from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, portas):
        super().__init__( placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__portas = portas

    def getPortas(self):
        return self.__portas
    
    def setPortas(self, portas):
        if portas <= 0:
            print("Número de portas Inválido")
        else:
            self.__portas = portas
    
    def imprimeCarro(self):
        super().imprime()
        print("Portas: " + str(self.__portas))
