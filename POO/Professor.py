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

def main():
    professor = Professor("kenia", 20220001, 15)
    professor.maisHoras(6)
    print(professor.getCarga())
    professor.menosHoras(8)
    print(professor.getCarga())
    professor.setNome("admilson")
    print(professor.getNome())
    professor = ProfessorUFS("admilson", 20220001, 15, 8, 20)
    professor.maisHoras(6)
    print(professor.getCarga())
    professor.menosHoras(8)
    print(professor.getCarga())
    professor.setNome("kenia")
    print(professor.getNome())
 
if __name__ == "__main__":
  main()