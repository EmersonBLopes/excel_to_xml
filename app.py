from Tabela import Tabela
from TagFactory import TagFactory
from XMLFactory import XMLFactory
from Field import Field

tb = Tabela("planilha_base.xlsx","Página2")
columns = ["AK","A","k","G","B","D"]#,["A","B","C"]
tags_names = ["title","city","price","url","description","contact"]#,"pictures"

field_list = []

for i in range(0,len(columns)):
    field_list.append(Field(columns[i],tags_names[i],True))
    
xml_builder = XMLFactory(field_list)
xml_builder.make_xml(tb.get_worksheet())
print(xml_builder.build())
    
#cria tag de anuncio e acrecenta dentro do conjuto ads
# for i in range(1,tb.get_worksheet().max_row): 

#     ad = TagFactory("ad")

#     for j in range(0,len(columns)):

#         ad.append_child(TagFactory(tags_names[j],tb.get_column(columns[j])[i].value,True))

#     ads.append_child(ad)

