class ProfessorUFS():
    def __init__(self, nome, matriculaSiape, cargaHoraria, horasMinimas, horasMaximas):
        self.__nome = nome
        self.__matriculaSiape = matriculaSiape
        self.__cargaHoraria = cargaHoraria
        self.__horasMinimas = horasMinimas
        self.__horasMaximas = horasMaximas

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
        self.__horas = horas
        if (self.__horasMaximas - self.__cargaHoraria) < self.__horas:
            print("Carga horária Máxima atinginda") 
        else:
            self.__cargaHoraria += horas
 
    def menosHoras(self, horas):
        self.__horas = horas
        if (self.__cargaHoraria - self.__horasMinimas) < self.__horas:
            print("Carga horária Mínima atinginda")
        else:
            self.__cargaHoraria -= horas