from produto import Produto
from impressora import Impressora
from cadastroProduto import CadastroProduto

def main():
    cadastro = CadastroProduto()
    produto1 = Produto("Celular", 63748, "iphone")
    impressora1 = Impressora("Eletronico", 25353, "Barato", "Boa", "samsung")
    impressora2 = Impressora("Eletronico", 26363, "LG", "Ruim", "Multilaser")
    cadastro.armazenar_produto(produto1)
    cadastro.armazenar_produto(impressora1)
    cadastro.armazenar_produto(impressora2)
    print(cadastro.listar_impressoras())

if __name__ == "__main__":
    main()