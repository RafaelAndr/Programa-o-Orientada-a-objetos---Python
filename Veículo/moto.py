from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, cilindrada):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__cilindradas = cilindrada

    def getCilindradas(self):
        return self.__cilindradas
    
    def setCilindradas(self, cilindradas):
        if cilindradas <= 0:
            print("Número de cilindradas Inválido")
        else:
            self.__cilindradas = cilindradas

    def imprimeMoto(self):
        super().imprime()
        print("Cilindradas: " + str(self.__cilindradas))