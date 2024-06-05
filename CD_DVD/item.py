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