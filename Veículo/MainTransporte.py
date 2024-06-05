from veiculo import Veiculo
from carro import Carro
from moto import Moto 
from bicicleta import Bicicleta

def main():
    carro = Carro("QKN-2039", "HONDA", 4, "CIVIC", 4)
    moto = Moto("QKY-4738", "YAMAHA", 2, "HORNET", 600)
    bicileta = Bicicleta("QJA-3847", "CALOI", 2, "EXPLORER", 21)
    carro.imprime()
    print("-------")
    moto.imprime()
    print("-------")
    bicileta.imprime()

if __name__ == "__main__":
    main()
