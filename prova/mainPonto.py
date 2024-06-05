from Ponto import Ponto 

def main():
    ponto = Ponto() 
    print(ponto.getX())
    print(ponto.getY())
    ponto.setX(5)
    ponto.setY(4)
    print(ponto.getX())
    print(ponto.getY())
    print(ponto.imprime())
    print(ponto.distanciaPontos(4,2))

if __name__ == "__main__":
    main()