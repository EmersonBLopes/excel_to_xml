from TagsNames import TagsNames
class Empreendimento:

    tags_name_list = TagsNames("title","url","description","email","category","price","city","contact")


    def __init__(self,title,url,price,description,city):

        self.__title = title
        self.__url = url
        self.__price = price
        self.__description = description
        self.__city = city
        self.__contact = "11 9832 78733"
        self.__email = "siteimovelnet@gmail.com"
        self.__category = "imóveis" 


    def __str__(self):
        return f"Titulo: {self.__title}\nUrl: {self.__url}\nPreço: {self.__price}\nDescrição: {self.__description}\nCidade: {self.__city}\nContato: {self.__contact}\ne-mail:{self.__email}\ncategoria:{self.__category}" 

    def __iter__(self):
        return Empreendimento.emprendimentos__list

    def get_title(self):
        
        return [self.__title,Empreendimento.tags_name_list.title]

    def get_url(self):
        
        return [self.__url,Empreendimento.tags_name_list.url]

    def get_price(self):
        
        return [self.__price,Empreendimento.tags_name_list.price]

    def get_description(self):
        
        return [self.__description,Empreendimento.tags_name_list.description]

    def get_city(self):
        
        return [self.__city,Empreendimento.tags_name_list.city]

    def get_contact(self):
        
        return [self.__contact,Empreendimento.tags_name_list.contact]

    def get_email(self):
        
        return [self.__email,Empreendimento.tags_name_list.email]

    def get_category(self):
        
        return [self.__category,Empreendimento.tags_name_list.category]
