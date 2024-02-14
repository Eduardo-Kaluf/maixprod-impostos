import requests
from datetime import datetime


class ErpController:
    def __init__(self, token) -> None:
        self.token = token
        self.notas = self.get_notas()
        self.operacoes = self.get_operacoes()
        self.ids = self.get_ids()
        self.notas_faturadas = self.get_faturas()

    def get_operacoes(self):
        url = "https://sistema.maxiprod.com.br/api/v1/OperacoesFiscais"

        result = requests.request("GET", url, params={"token": self.token})

        return (result.json())

    def get_notas(self):

        url = "https://sistema.maxiprod.com.br/api/v1/Notas"

        result = requests.request("GET", url, params={"token": self.token})

        return result.json()

    def get_ids(self):
        operacoes = self.operacoes
        ids = []

        for operacao in operacoes["Registros"]:
            if operacao["Tipo"] == "Faturamento":
                ids.append(operacao["Operacao_fiscal_Id"])

        return ids

    def get_faturas(self):
        notas = self.notas
        ids = self.ids
        notas_faturadas = []

        for registro in notas["Registros"]:
            if registro["Operacao_fiscal_Id"] in ids and registro["Estado"] == "Emitida":
                notas_faturadas.append(registro)

        return notas_faturadas

    def _date_converter(self, dicionario):
        date_str = dicionario["Data"]
        date_format = "%d/%m/%Y"
        date_obj = datetime.strptime(date_str, date_format)

        return date_obj

    def receitas_por_mes(self, year):

        # Substituir lista por deque, para o pop(0) ficar mais efetivo

        notas_faturadas = self.notas_faturadas

        messes = []
        total_mes = 0
        lista_notas = notas_faturadas.copy()
        counter = 12

        for i in notas_faturadas:

            date_obj = self._date_converter(i)

            if date_obj.year > year:
                lista_notas.pop(0)
            else:
                break

        notas_faturadas = lista_notas.copy()

        while counter != 0:
            if notas_faturadas:
                for nota in notas_faturadas:
                    date_obj = self._date_converter(nota)
                    if date_obj.month == counter:
                        if not lista_notas:
                            notas_faturadas = lista_notas.copy()
                            messes.append(total_mes)
                            counter -= 1
                            break

                        total_mes += nota["Valor_total"]

                        lista_notas.pop(0)
                    else:
                        notas_faturadas = lista_notas.copy()
                        messes.append(total_mes)
                        counter -= 1
                        total_mes = 0
                        break
            else:
                for i in range(0, counter):
                    messes.append(0)
                break

        return messes[::-1]

    def get_tabela(self, ano):
        receitas_atuais = self.receitas_por_mes(ano)
        receitas_anteriores = self.receitas_por_mes(ano - 1)

        tabela_receitas = {ano: {},
                     (ano - 1): {}
        }

        receitas_por_ano = [receitas_atuais, receitas_anteriores]
        receitas_combinadas = receitas_anteriores + receitas_atuais

        for i in range(0, 2):
            receita_acumulada = 0
            receita_bruta_apurada = 0
            rbt12 = 0
            for j in range(1, 13):

                receita_bruta_apurada = receitas_por_ano[i][j - 1]

                if j != 1:
                    receita_acumulada += receitas_por_ano[i][j - 2]

                if i != 1:
                    inicio = j - 1
                    fim = j + 11
                    temp = receitas_combinadas[inicio:fim]
                    rbt12 = sum(list(temp))

                temp = {j: {
                        "receita_bruta_apurada": receita_bruta_apurada,
                        "receita_bruta_acumulada": receita_acumulada,
                        "rbt12": rbt12
                    }}

                tabela_receitas[ano - i].update(temp)

        return tabela_receitas
