from item import Item

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