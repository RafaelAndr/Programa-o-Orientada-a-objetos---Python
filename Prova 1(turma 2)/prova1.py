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

class Plano:
    def __init__(self):
        self.__pontos = []

    def inserir(self,ponto):
        self.__pontos.append(ponto)

    def remove(self,ponto):
        if ponto in self.__pontos:
            self.__pontos.remove(ponto)

    def listar(self):
        contador = 0
        while contador < len(self.__pontos):
            print(self.__pontos)
            contador += 1

    def verificaPonto(self, p):
        for ponto in self.__pontos:
            if ponto == p:
                return True
            else:
                return False
            
def main():
    ponto = Ponto() 
    print(ponto.getX())
    print(ponto.getY())
    ponto.setX(5)
    ponto.setY(4)
    print(ponto.getX())
    print(ponto.getY())
    print(ponto.imprime())
    ponto.distanciaPontos(4,2)
    plano = Plano()
    plano.inserir(2)
    plano.inserir(3)
    plano.inserir(4)
    plano.remove(3)
    plano.listar()
    print(plano.verificaPonto(2))

if __name__ == "__main__":
    main()