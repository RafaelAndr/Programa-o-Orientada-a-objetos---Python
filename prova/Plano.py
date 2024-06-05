from Ponto import Ponto

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