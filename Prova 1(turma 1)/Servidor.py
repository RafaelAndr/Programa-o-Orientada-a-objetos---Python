import random

class ServidorPublico:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
        self.__matricula = random.randint(1,9999)
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novoNome):
        self.__nome = novoNome
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, novoSalario):
        self.__salario = novoSalario

    def get_matricula(self):
        return self.__matricula
    
    def exibir_atributos(self):
        print("Nome: ", self.__nome)
        print("Salário: ", self.__salario)
        print("Matrícula: ", self.__matricula)

class Servidor:
    def __init__(self):
        self.lista = []

    def adicionar(self, objeto):
        self.lista.append(objeto)

    def remover(self, objeto):
        self.lista.remove(objeto)

    def listar(self):
        for objeto in self.lista:
            objeto.exibir_atributos()

def main():
    servidor1 = ServidorPublico("José", 2500)
    print(servidor1.get_matricula())
    servidor1.exibir_atributos()
    servidor = Servidor()   
    servidor1 = ServidorPublico("José", 3000)
    servidor2 = ServidorPublico("João", 2000)
    servidor.adicionar(servidor1)
    servidor.adicionar(servidor2)
    servidor.remover(servidor1)
    servidor.listar()


if __name__ == "__main__":
    main()