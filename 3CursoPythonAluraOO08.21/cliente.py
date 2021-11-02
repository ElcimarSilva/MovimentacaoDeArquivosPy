class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamado @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamado @property nome()")
        self.__nome = nome
