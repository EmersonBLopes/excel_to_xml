from Tabela import Tabela
from Empreendimento import Empreendimento

tb = Tabela("planilha_base.xlsx","Página2")

emprendimentos__list = []

#Construindo a lista de empreendimetos
for i in range(2, tb.get_worksheet().max_row+1):
    emprendimentos__list.append(Empreendimento(
        tb.get_worksheet()[f"AK{i}"].value,
        tb.get_worksheet()[f"G{i}"].value,
        tb.get_worksheet()[f"K{i}"].value,
        tb.get_worksheet()[f"B{i}"].value,
        tb.get_worksheet()[f"A{i}"].value,
        ))

for empreendimento in emprendimentos__list:
    print(f"\n{empreendimento}")
