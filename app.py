from Tabela import Tabela
from TagFactory import TagFactory
from XMLFactory import XMLFactory
from Field import Field

tb = Tabela("planilha_base.xlsx","Página2")
columns = ["AK","A","k","G","B","D",["E","F","G"]]
tags_names = ["title","city","price","url","description","contact","pictures"]

field_list = []

for i in range(0,len(columns)):

    if type(columns[i]) != list:
        field_list.append(Field(columns[i],tags_names[i],True))
    else:
        for column in columns[i]:
            field_list.append(Field(columns[i],"url_img",True))
    
xml_builder = XMLFactory(field_list,tb.get_worksheet())
xml_builder.make_xml()
print(xml_builder.build())
