class TagFactory:

    def __init__(self,data):
        self.__data = data

    def __str__(self):
        return f"<{self.__data[1]}>![CDATA[{self.__data[0]}]]</{self.__data[1]}>"
