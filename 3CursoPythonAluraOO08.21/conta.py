class Conta:
    def __init__(self, numero, titular, saldo, limite):  # método contrutor com os atributos que devem ser passados objt
        print(f"Contruindo objeto ... {self}")  # na criação de um novo objeto deve ter as caracteriscas iu atributos
        self.__numero = numero  # atributos privados do método
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de R${self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self): # get pega um valor
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite): # set altera um valor
        self.__limite = limite
