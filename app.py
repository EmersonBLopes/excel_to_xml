from Tabela import Tabela
from Empreendimento import Empreendimento
from TagFactory import TagFactory

tb = Tabela("planilha_base.xlsx","Página2")

ads = TagFactory("ads")
ad = TagFactory("ad")

ads.append_child(TagFactory("teste","teste"))

for city in tb.get_column("A",2):
    ad.append_child(TagFactory("city",city.value,True))

#ads.append_child(ad)
ads.append_child(ad)

print(ads)
