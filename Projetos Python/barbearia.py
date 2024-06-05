# criar um sistema de gerenciamento de uma barbearia, no sistema deve conter:
# dados de cada barbeiro(tempo de experiencia, numero de cabelo cortados, total faturado),
# dados dos equipamento(nome, preço, função), 
# dados da barbearia(localização, impostos, serviços, preços) 
# dados de cada cliente(nome, tipo de corte, categoria)

class barbearia:
    def __init__(self, localização):
        self.__localização = "Rua padre Alvares Pitangueira, 287"

    def imposto(self, tipo_empresa):
        self.tipo_empresa = tipo_empresa
        if tipo_empresa == "Grande":
            return 250
        elif tipo_empresa == "Media":
            return 200
        elif tipo_empresa == "pequena":
            return 150
        else:
            print("tipo não reconhecido")

    def serviços(self):
        lista_serviços = ["corte = 20,00 reais", "Sobrancelha = 5,00 reais", "barba = 15,00 reais"]
        for i in enumerate (1, lista_serviços):
            print(i)
        