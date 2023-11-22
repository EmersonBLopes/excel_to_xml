from openpyxl import load_workbook

class Tabela:

    def __init__(self, workbook, worksheet):

        self.__workbook = load_workbook(workbook)
        self.__worksheet = self.__workbook[worksheet]
        

    @property
    def max_row(self):
        
        row_count = 1
        empty_row = False

        while(not(empty_row)):
            
            i = 1

            while(True):

                empty_row = True
                i += 1

                for cell in self.get_row(i):

                    if(cell.value != None):
                        empty_row = False

                if empty_row:
                    break

                row_count += 1

        return row_count

    def get_row(self,row):
        return self.__worksheet[row]

    def get_column(self, column, start=1):
        return self.__worksheet[column] 

    def get_cell(self,cell_coordinate):
        return self.__worksheet[cell_coordinate].value

    def get_worksheet(self):
        return self.__worksheet

