from TagFactory import TagFactory
from Tabela import Tabela
from Field import Field

class XMLFactory:

    def __init__(self,field_list,worksheet):

        self.__field_list = field_list
        self.__body = [TagFactory(declaration_tag=True)]
        self.__worksheet = worksheet
        

    def genarate_xml(self):

        output = ""

        for tag in self.__body:
            output += str(tag)


        with open("saida.xml","w",encoding="utf-8") as file:
            file.write(output)

    def __make_set(self,set,row):

        parent = TagFactory("pictures")
        for column in set.column:
            parent.append_child(TagFactory("url_img",self.__worksheet[f"{column}{row}"].value,True))

        return parent

        


    def make_ads(self):

        ads = TagFactory("ads")

        for i in range(2,self.__worksheet.max_row):

            ad = TagFactory("ad")

            for j in range(0,len(self.__field_list)):

                if type(self.__field_list[j].column) != list:
                    ad.append_child(TagFactory(self.__field_list[j].tag_name,self.__worksheet[self.__field_list[j].column][i].value,self.__field_list[j].cdata))
                else:
                    ad.append_child(self.__make_set(self.__field_list[j],i))
                    break

            ads.append_child(ad)

        self.__body.append(ads)
