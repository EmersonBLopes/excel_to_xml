class Field:

    def __init__(self,column,tag_name,cdta):
        self.__column = column
        self.__tag_name = tag_name
        self.__cdta = cdta
    
    @property
    def column(self):
        return self.__column

    @property
    def tag_name(self):
        return self.__tag_name

    @property
    def cdata(self):
        return self.__cdta
    
    def __str__(self):
        return f"Column:{self.__column}\nTag:{self.__tag_name}\ncdata:{self.__cdta}"
