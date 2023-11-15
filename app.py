from Tabela import Tabela
from Empreendimento import Empreendimento
from TagFactory import TagFactory

tb = Tabela("planilha_base.xlsx","Página2")

ads = TagFactory("ads")
ads.append_child(TagFactory("ad"))
ads.append_child(TagFactory("teste","teste"))

for city in tb.get_column("A",2):
    ads.get_child(0).append_child(TagFactory("city",city.value,True))

#ads.append_child(ad)

print(ads)
