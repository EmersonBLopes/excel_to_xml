from Tabela import Tabela

tb = Tabela("planilha_base.xlsx","Página2")

for cell in tb.get_column("A"):
    print(cell.value)
