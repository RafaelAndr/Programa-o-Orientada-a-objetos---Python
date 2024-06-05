class Item:
    def __init__(self, titulo, tempRep, pos, coment):
        self.__titulo = self.setTitulo(titulo)
        self.__tempoDeReproducao = self.setTempo(tempRep)
        self.__possuo =  self.setPossuo(pos)
        self.__comentario = self.setComentario(coment)

    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, titulo):
        if type(titulo) == str:
            self.__titulo = titulo
            return titulo
        return None

    def getTempo(self):
        return self.__tempoDeReproducao
    
    def setTempo(self, tempo):
        if type(tempo) == int:
            self.__tempoDeReproducao = tempo
            return tempo
        return None

    def getPossuo(self):
        return self.__possuo
    
    def setPossuo(self, possuo):
        if type(possuo) == bool:
            self.__possuo = possuo
            return True
        return None

    def getComentario(self):
        return self.__comentario
    
    def setComentario(self, comentario):
        if type(comentario) == str:
            self.__comentario = comentario
            return comentario
        return None

class CD(Item):
    def __init__(self, titulo, tempRep, art, numTri, pos, coment):
        super().__init__(titulo, tempRep, pos, coment)
        self.__artista = self.setArtista(art)
        self.__numeroDeTrilhas = self.setNumeroDeTrilhas(numTri)

    def getArtista(self):
        return self.__artista
    
    def setArtista(self, artista):
        self.__artista = artista
        if type(artista) == str:
            self.__artista = artista
            return artista
        return None

    def getNumeroDeTrilhas(self):
        return self.__numeroDeTrilhas
    
    def setNumeroDeTrilhas(self, numeroDeTrilhas):
        self.__numeroDeTrilhas = numeroDeTrilhas
        if type(numeroDeTrilhas) == int:
            self.__numeroDeTrilhas = numeroDeTrilhas
            return numeroDeTrilhas
        return None

    def imprimirCD(self):
        print('Titulo: {}'.format(self.getTitulo()))
        print('Tempo de reproducao: {}'.format(self.getTempo()))
        print('Artista: {}'.format(self.getArtista()))
        print('Numero de trilhas: {}'.format(self.getNumeroDeTrilhas()))
        if(self.getPossuo()):
            print('Possuo.')
        else:
            print('Nao possuo')
        print('Comentário: {}'.format(self.getComentario()))


class DVD(Item):
    def __init__(self, titulo, tempRep, diretor, pos, coment):
        super().__init__(titulo, tempRep, pos, coment)
        self.__diretor = self.setDiretor(diretor)
    
    def getDiretor(self):
        return self.__diretor
    
    def setDiretor(self, dir):
        self.__diretor = dir
        if type(dir) == str:
            self.__diretor = dir
            return dir
        return None

    def imprimirDVD(self):
        print('Titulo: {}'.format(self.getTitulo()))
        print('Tempo de reproducao: {}'.format(self.getTempo()))
        print('Diretor: {}'.format(self.getDiretor()))
        if(self.getPossuo()):
            print('Possuo.')
        else:
            print('Nao possuo.')
        print('Comentário: {}'.format(self.getComentario()))

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
                item.imprimirCD()
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

def main():

    catalogo1 = Catalogo()
    cd1 = CD("CD 1", 90, "Artista 1", 13, True, "Top")
    dvd1 = DVD("DVD 1", 90, "Artista 2", True, "Top")

    catalogo1.inserirItem(cd1)
    catalogo1.inserirItem(dvd1)
    # catalogo1.removerItem(dvd1)
    print(catalogo1.listarItens())

if __name__ == "__main__":
    main()