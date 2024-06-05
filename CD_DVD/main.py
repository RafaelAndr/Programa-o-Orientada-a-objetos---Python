from catalogo import Catalogo
from cdheranca import CD
from dvdheranca import DVD


def main():

    catalogo1 = Catalogo()
    cd1 = CD("CD 1", 90, "Artista 1", 13, True, "Top")
    dvd1 = DVD("DVD 1", 90, "Artista 2", True, "Top")

    catalogo1.inserirItem(cd1)
    catalogo1.inserirItem(dvd1)
    # catalogo1.removerItem(dvd1)
    print(catalogo1.listarItens())

if __name__ == "__main__":
    main()