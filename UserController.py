from Field import Field

class UserController:

    def create_fields(self):

        columns = ["B","G","D","A","C","F","E",["J","K","L","M"]]
        tags_names = ["title","city","price","url","description","contact","email","pictures"]

        field_list = []

        for i in range(0,len(columns)):

            if type(columns[i]) != list:
                field_list.append(Field(columns[i],tags_names[i],True))
            else:
                for column in columns[i]:
                    field_list.append(Field(columns[i],"url_img",True))
            
        return field_list

    #def write_file(self,str):
