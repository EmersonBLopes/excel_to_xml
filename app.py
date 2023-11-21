from Tabela import Tabela
from UserController import UserController
from TagFactory import TagFactory
from XMLFactory import XMLFactory

flag = False
user = UserController()

while(not(flag)):

    planilha = "BDI.xlsx"#input("Digite o nome da planilha que deseja trabalhar:")
    pagina =   "DADOS SEM FORMULA"#input("Digite o nome da pagina que deseja trabalhar:")

    try:
        tb = Tabela(planilha,pagina)
        flag = True 

    except Exception as ex:

        if type(ex) == KeyError:
            print("Pagina não encontrada.")
        else:
            print("Planilha não encontrada.")


print(tb.max_row)
xml_builder = XMLFactory(user.create_fields(),tb)
xml_builder.make_ads()

xml_builder.genarate_xml()
