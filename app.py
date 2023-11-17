from Tabela import Tabela
from Empreendimento import Empreendimento
from TagFactory import TagFactory

tb = Tabela("planilha_base.xlsx","Página2")
columns = ["AK","A","k","G","B"]
tags_names = ["title","city","price","url","Description"]

ads = TagFactory(declaration_tag=True)

#cria tag de anuncio e acrecenta dentro do conjuto ads
# for i in range(1,tb.get_worksheet().max_row): 

#     ad = TagFactory("ad")

#     for j in range(0,len(columns)):

#         ad.append_child(TagFactory(tags_names[j],tb.get_column(columns[j])[i].value,True))

#     ads.append_child(ad)

print(ads)
