from openpyxl import load_workbook

class Tabela:

    def __init__(self, workbook, worksheet):

        self.__workbook = load_workbook(workbook)
        self.__worksheet = self.__workbook[worksheet]
        

    def get_row(self,row):
        return self.__worksheet[row]

    def get_column(self, column, start=1):
        return self.__worksheet[column] 

    def get_cell(self,cell_coordinate):
        return self.__worksheet[cell_coordinate].value

    def get_worksheet(self):
        return self.__worksheet

