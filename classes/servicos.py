import sys
sys.path.append(r'C:\Users\Luis\Desktop\Programacao\iotag')
from src.constantes import FaixasTerceiroAnexo, FaixasQuintoAnexo, FaixasPrimeiroAnexo


# rbt12 -> Receita Bruta 12 messes anteriores
# PRA -> "Percentual de Redução Anexo I – Comércio"
# PRA será definido como uma constante, por enquanto

PRA = 0.3658


class Servicos:
    def __init__(self, rbt12, anexo) -> None:
        self.rbt12 = rbt12
        self.faixa = self.encontra_faixa()
        match anexo:
            case 1:
                dados = FaixasPrimeiroAnexo[self.faixa].value
            case 3:
                dados = FaixasTerceiroAnexo[self.faixa].value
            case 5:
                dados = FaixasQuintoAnexo[self.faixa].value
        self.aliquota = dados["aliquota"]
        self.deducao = dados["deducao"]
        self.iss = dados["iss"]

    def icms_anexo_um(self):
        dados = FaixasPrimeiroAnexo[self.faixa].value
        return (((self.rbt12 * dados["aliquota"] - dados["deducao"]) / self.rbt12) * dados["icms"])

    def servicos(self):
        return round(((self.rbt12 * self.aliquota) - self.deducao) / self.rbt12, 7)

    def locacao(self):
        return round((self.servicos() * (1 - self.iss)), 7)

    def comunicacao(self):
        return round(self.locacao() + self.icms_anexo_um(), 7)

    def comunicacao_pr(self):
        return round(self.locacao() + self.icms_anexo_um() * (1 - PRA), 7)

    def servicos_ISS(self):
        return round((self.servicos() * self.iss), 7)

    def encontra_faixa(self):
        if self.rbt12 <= 180000:
            return "PRIMEIRA"
        elif self.rbt12 > 180000 and self.rbt12 <= 360000:
            return "SEGUNDA"
        elif self.rbt12 > 360000 and self.rbt12 <= 720000:
            return "TERCEIRA"
        elif self.rbt12 > 720000 and self.rbt12 <= 1800000:
            return "QUARTA"
        elif self.rbt12 > 1800000 and self.rbt12 <= 3600000:
            return "QUINTA"
        else:
            return "SEXTA"
