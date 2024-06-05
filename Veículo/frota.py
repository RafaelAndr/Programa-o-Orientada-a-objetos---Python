from veiculo import Veiculo

class Frota:
    def __init__(self):
        self.__frota = list()

    def inserirVeiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__frota.append(veiculo)
        else:
            print("Erro: o objeto passado nao é do tipo Veiculo.")

    def removerVeiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__frota.remove(veiculo)
        else:
            print("Erro: o objeto passado nao é do tipo Veiculo.")
    
    def listarVeiculos(self):
        print(f"Numero de veiculos: {len(self.__frota)}\n")
        for veiculo in self.__frota:
            veiculo.imprime()

    def localizarVeiculo(self, placa):
        for veiculo in self.__frota:
            if veiculo.getPlacaVeiculo() == placa:
                veiculo.imprime()