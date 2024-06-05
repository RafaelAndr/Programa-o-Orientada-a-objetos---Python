from produto import Produto
from impressora import Impressora

class CadastroProduto():
    def __init__(self):
        self.__produtos = list()

    def armazenar_produto(self, produto):
        self.__produtos.append(produto)

    def listar_impressoras(self):
        for produto in self.__produtos:
            if isinstance(produto, Impressora):
                produto.imprime_produto()