class TagFactory:

    def __init__(self,name="",data=None,cdata=False,declaration_tag=False):
        self.__name = name
        self.__data = data
        self.__cdata = cdata
        self.__children = []
        self.__indentation_space = 0
        self.__declaration_tag = declaration_tag

    def __str__(self):

        msg = self.to_ident(self.__indentation_space) 

        if self.__declaration_tag:
            return "<?xml version='1.0' encoding='UTF-8'?>"
        #return if cdata
        if self.__cdata:
            msg += f"<{self.__name}>![CDATA[{self.__data}]]</{self.__name}>"
            return msg


        #return with children
        if len(self.__children) != 0:

            msg += f"<{self.__name}>\n"
            for child in self.__children:

                msg += str(child) + "\n"

            msg += self.to_ident(self.__indentation_space)
            msg += f"</{self.__name}>"
        else:
            msg += f"<{self.__name}>{self.__data}</{self.__name}>"

        return msg

    def to_ident(self,tab_count):

        msg = ""
        for i in range(0, tab_count):
            msg += "\t"

        return msg
        

    def set_identation(self,value):
        self.__indentation_space = value


    def get_child(self,child_number):
        return self.__children[child_number]

    def append_child(self,element):

        element.set_identation(self.__indentation_space + 1)

        for child in element.__children:
            child.set_identation(element.__indentation_space+1)

        self.__children.append(element)
