from cdheranca import CD
from dvdheranca import DVD

class Catalogo:
    def __init__(self):
        self.__itens = list()

    def inserirItem(self, item):
        if item not in self.__itens:
            self.__itens.append(item)
        else:
            return False

    def removerItem(self, item):
        if item in self.__itens:
            self.__itens.remove(item)
            return True
        return False

    def listarItens(self):
        for item in self.__itens:
            if (isinstance(item, CD)):
                print("------------")
                print("Tipo: CD")
                item.
            if (isinstance(item, DVD)):
                print("------------")
                print("Tipo: DVD")
                item.imprimirDVD()

    def localizarItem(self, titulo):
        for item in self.__itens:
            if(titulo == item.getTitulo()):
                if (isinstance(item, CD)):
                    item.imprimirCD()
                if (isinstance(item, DVD)):
                    item.imprimirDVD()