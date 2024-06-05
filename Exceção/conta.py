class Conta:

    def __init__(self, nomeCorrentista, numeroConta):
        self.__nomeCorrentista = ""
        self.__numeroConta = 0
        self.__saldo = 0
        self.__ativa = True
        self.setNomeCorrentista(nomeCorrentista)
        self.setNumeroConta(numeroConta)

    def imprimeConta(self):
        print(self.getNomeCorrentista())
        print(self.getNumeroConta())
        print(self.getSaldo())
        print(self.getAtiva())

    def deposito(self, valor):
        if (valor < 0):
            raise ValueError("O valor deve ser positivo")
        else:
            self.__saldo = self.__saldo + valor

    def saque(self, valor):
        if (valor < 0):
            raise ValueError("O valor deve ser positivo")
        elif(valor > self.__saldo):
            raise ValueError("Saldo Insuficiente")
        else:
            self.__saldo = self.__saldo - valor
            print(f'Você sacou R${valor}')
            print(f'Novo Saldo R${self.__saldo}')
    
    def getNomeCorrentista (self):
        return self.__nomeCorrentista
    
    def setNomeCorrentista(self, nomeCorrentista):
        if nomeCorrentista == "":
            raise ValueError("O nome do correntista nao pode ser vazio")
        elif type(nomeCorrentista) != str:
            raise ValueError("O nome do correntista deve ser string")
        else:
            self.__nomeCorrentista = nomeCorrentista
    
    def getNumeroConta (self):
        return self.__numeroConta
    
    def setNumeroConta (self, numeroConta):
        if numeroConta <= 0:
            raise ValueError("O numero da conta nao pode ser negativo")
        elif type(numeroConta) != int:
            raise ValueError("O numero da conta deve ser um inteiro")
        else:
            self.__numeroConta = numeroConta

    def getSaldo (self):
        return self.__saldo
    
    def setSaldo (self, saldo):
        self.__saldo = saldo

    def getAtiva (self):
        return self.__ativa
    
    def setAtiva (self, ativa):
        self.__ativa = ativa