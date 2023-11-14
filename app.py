from Tabela import Tabela
from Empreendimento import Empreendimento
from TagFactory import TagFactory

tb = Tabela("planilha_base.xlsx","Página2")

emprendimentos_list = []

#Construindo a lista de empreendimetos
for i in range(2, tb.get_worksheet().max_row+1):
    emprendimentos_list.append(Empreendimento(
        tb.get_worksheet()[f"AK{i}"].value,
        tb.get_worksheet()[f"G{i}"].value,
        tb.get_worksheet()[f"K{i}"].value,
        tb.get_worksheet()[f"B{i}"].value,
        tb.get_worksheet()[f"A{i}"].value,
        ))

tags_list = []
for empreendimento in emprendimentos_list:
    tags_list.append(TagFactory(empreendimento.get_title()))
    tags_list.append(TagFactory(empreendimento.get_email()))
    tags_list.append(TagFactory(empreendimento.get_contact()))
    tags_list.append(TagFactory(empreendimento.get_url()))
    tags_list.append(TagFactory(empreendimento.get_price()))
    tags_list.append(TagFactory(empreendimento.get_category()))
    tags_list.append(TagFactory(empreendimento.get_city()))
    tags_list.append(TagFactory(empreendimento.get_description()))
    

for i in range(0, 8):
    print(tags_list[i])
