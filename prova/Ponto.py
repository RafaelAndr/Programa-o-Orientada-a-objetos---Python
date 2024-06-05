import math

class Ponto:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def getX(self):
        return self.__x
    
    def setX(self, NovoX):
        self.__x = NovoX
    
    def getY(self):
        return self.__y
    
    def setY(self, NovoY):
        self.__y = NovoY
    
    def imprime(self):
        print("Ponto X:", self.__x)
        print("Ponto Y:", self.__y)

    def distanciaPontos(self,pX,pY):
        quadradoX = ((self.__x - pX)**2)
        quadradoY = ((self.__y - pY)**2)
        return math.sqrt(quadradoX + quadradoY)

