import sys
sys.path.append(r'C:\Users\Luis\Desktop\Programacao\iotag')
from variaveis_ambiente import ERP_KEY
from classes.servicos import Servicos
from classes.erp_controller import ErpController


controller = ErpController(ERP_KEY)

tabela = controller.get_tabela(2023)

# Pelo fato dos valores inseridos no ERP estarem incompletos, um payload com os valores reais sera utilizado no lugar
payload = [
    1063779.71,
    1202449.30,
    1295493.89,
    1390808.54,
    1474393.41,
    1503571.73,
    1584762.40,
    1571632.09,
    1565207.49,
    1599541.61,
    1651945.03,
    1450282.98
]

# O codigo real, para o calculo da aliquota de serviço ficaria assim
"""
for i in range(1, 12):
    temp = Servicos(tabela[2023][i]["rbt12"], 3)
    print(temp.servicos())
"""

# Para fins de teste faremos assim
for i in payload:
    temp = Servicos(i, 3)
    print(temp.servicos())
