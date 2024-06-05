class Professor():
    def __init__(self, nome, matriculaSiape, cargaHoraria):
        self.__nome = nome
        self.__matriculaSiape = matriculaSiape
        self.__cargaHoraria = cargaHoraria

    def getNome(self):
        return self.__nome
 
    def setNome(self, novoNome):
        self.__nome = novoNome

    def getMatricula(self):
        return self.__matriculaSiape
   
    def setMatricula(self, novaMatricula):
        self.__matriculaSiape = novaMatricula

    def getCarga(self):
        return self.__cargaHoraria
 
    def setCarga(self, novaCarga):
        self.__cargaHoraria = novaCarga
 
    def maisHoras(self, horas):
        self.horas = horas
        self.__cargaHoraria += horas
 
    def menosHoras(self, horas):
        self.horas = horas
        self.__cargaHoraria -= horas