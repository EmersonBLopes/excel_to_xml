class Empreendimento:

    def __init__(self,title,url,price,description,city,category):

        self.__title = title
        self.__url = url
        self.__price = price
        self.__description = description
        self.__city = city
        self.__contact = "11 9832 78733"
        self.__email = "siteimovelnet@gmail.com"
        self.__category = "imóveis" 

        self.emprendimentos__list = []

    def __str__(self):
        return f"Titulo: {self.__title}\nUrl: {self.__url}\nPreço: {self.__price}\n Descrição: {self.__description}\nCidade: {self.__city}\nContato: {self.__contact}\ne-mail:{self.__email}\ncategoria:{self.__category}" 

    def get_title(self):
        
        return self.__title

    def get_url(self):
        
        return self.__url

    def get_price(self):
        
        return self.__price

    def get_description(self):
        
        return self.__description

    def get_city(self):
        
        return self.__city

    def get_contact(self):
        
        return self.__contact

    def get_email(self):
        
        return self.__email

    def get_category(self):
        
        return self.__category


    def add_empreendimento(self,empreendimento):

        self.emprendimentos__list.append(empreendimento)

    def get_lista_empreendimentos(self):

        return emprendimentos__list