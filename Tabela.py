from openpyxl import load_workbook

class Tabela:

    def __init__(self, workbook, worksheet):

        self.__workbook = load_workbook(workbook)
        self.__worksheet = self.__workbook[worksheet]
        

    def get_row(self,row_index):
        return self.__worksheet[row_index]

