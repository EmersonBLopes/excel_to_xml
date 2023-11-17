from TagFactory import TagFactory
from Tabela import Tabela
from Field import Field

class XMLFactory:

    def __init__(self,field_list):

        self.__field_list = field_list
        self.__contact = "(11) 123-456"
        self.__body = []

    def build(self):

        msg = ""

        for tag in self.__body:
            msg += str(tag)

        return msg 

    def make_xml(self,worksheet):
        ads = TagFactory("ads")

        for i in range(2,worksheet.max_row):

            ad = TagFactory("ad")

            for j in range(0,len(self.__field_list)):
                ad.append_child(TagFactory(self.__field_list[j].tag_name,worksheet[self.__field_list[j].column][i].value,self.__field_list[j].cdata))

            ads.append_child(ad)

        self.__body.append(ads)

    #    #cria tag de anuncio e acrecenta dentro do conjuto ads
    #    for i in range(1,tb.get_worksheet().max_row): 

    #        child = TagFactory(child_name)

    #        for j in range(0,len(self.__columns)):

    #            if(self.__columns[j] == list):


    #            ad.append_child(TagFactory(tags_names[j],tb.get_column(columns[j])[i].value,True))

    #        parent.append_child(ad)

    
