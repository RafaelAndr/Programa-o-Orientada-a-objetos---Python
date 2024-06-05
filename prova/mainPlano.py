from Plano import Plano
from Ponto import Ponto 

def main():
    plano = Plano()
    plano.inserir(2)
    plano.inserir(3)
    plano.inserir(4)
    plano.remove(3)
    plano.listar()
    print(plano.verificaPonto(2))

if __name__ == "__main__":
    main()