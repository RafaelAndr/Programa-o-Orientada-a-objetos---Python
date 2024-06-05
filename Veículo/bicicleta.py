from veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, marchas):
        super().__init__( placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__marchas = marchas

    def getMarchas(self):
        return self.__marchas
    
    def setMarchas(self, marchas):
        if marchas <= 0:
            print("Número de marchas Inválido")
        else:
            self.__marchas = marchas

    def imprimeBicicleta(self):
        super().imprime()
        print("Marchas: " + str(self.__marchas))