from frota import Frota
from carro import Carro
from moto import Moto 
from bicicleta import Bicicleta

def main():
    frota = Frota()
    carro1 = Carro("QKN-2039", "HONDA", 4, "CIVIC", 4)
    moto1 = Moto("QKY-4738", "YAMAHA", 2, "HORNET", 600)
    bicileta1 = Bicicleta("QJA-3847", "CALOI", 2, "EXPLORER", 21)
    frota.inserirVeiculo(carro1)
    frota.inserirVeiculo(moto1)
    frota.inserirVeiculo(bicileta1)
    frota.removerVeiculo(carro1)
    frota.listarVeiculos()

if __name__ == "__main__":
    main()