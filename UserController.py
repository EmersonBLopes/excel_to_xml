from Tabela import Tabela
from Field import Field
from XMLFactory import XMLFactory

class UserController:

    def __init__(self):

        self.set_workbook()
        self.__xml_builder = None
        self.__field_list = []
        self.create_fields()

    def display_menu(self):

        while(True):

            #display menu
            with open("menu.txt") as msg:
                print(msg.read())

            opcao = input("Digite uma opção:")

            if(opcao == "1"):
                self.set_workbook()
            elif(opcao == "3"):
                self.create_fields()
            elif(opcao == "4"):
                self.generate_XML()


    def set_workbook(self):

        flag = False

        while(not(flag)):

            self.__workbook = input("Digite o nome da planilha:") 
            self.__worksheet = input("Digite a pagina que deseja trabalhar:")


            try:
                self.__tb = Tabela(self.__workbook,self.__worksheet)
                flag = True 

            except Exception as ex:

                if type(ex) == KeyError:
                    print("Pagina não encontrada.")
                else:
                    print(f"Planilha não encontrada. {ex}")


        self.__tb = Tabela(self.__workbook,self.__worksheet)

    def create_fields(self):

        print("criando campos")
        columns = ["B","G","D","A","C","F","E",["J","K","L","M"]]
        tags_names = ["title","city","price","url","description","contact","email","pictures"]

        for i in range(0,len(columns)):

            if type(columns[i]) != list:
                self.__field_list.append(Field(columns[i],tags_names[i],True))
            else:
                for column in columns[i]:
                    self.__field_list.append(Field(columns[i],"url_img",True))
            

    def generate_XML(self):
        self.__xml_builder = XMLFactory(self.__field_list,self.__tb)
        print("gerando XML...")
        self.__xml_builder.genarate_xml()
