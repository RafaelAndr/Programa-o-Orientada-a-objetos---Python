from item import Item

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