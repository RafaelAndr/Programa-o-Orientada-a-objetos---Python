from produto import Produto

class Impressora(Produto):
    def __init__(self, tipo_produto, codigo_produto, descricao_produto, modelo, tipo_impressora):
        super().__init__(tipo_produto, codigo_produto, descricao_produto)
        self.__tipo = self.set_tipo(tipo_impressora)
        self.__modelo = self.set_modelo(modelo)
        self.__disponibilidade = 0
        self.__estoque = True

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, NovoModelo):
        self.__modelo = NovoModelo

    def get_tipoimpressora(self):
        return self.__modelo
    
    def set_tipoimpressora(self, novoTipo):
        self.__tipo = novoTipo

    def get_disponibilidade(self):
        return self.__disponibilidade
    
    def get_estoque(self):
        if self.__disponibilidade > 0:
            return True
        else:
            return False

    def aumenta_estoque(self, quantidade):
        if quantidade == "":
            raise ValueError("Quantidade não pode ser vazia")
        elif quantidade < 0:
            raise ValueError("Valor não pode ser negativo")
        else:
            self.__disponibilidade += quantidade

    def diminui_estoque(self, quantidade):
        if self.__disponibilidade == 0:
            print("Estoque vazio")
        elif quantidade == "":
            raise ValueError("Quantidade não pode ser vazia")
        elif quantidade < 0:
            raise ValueError("Valor não pode ser negativo")
        else:
            self.__disponibilidade -= quantidade

    def imprime_produto(self):
        super().imprime_produto()
        print("modelo: " + str(self.__modelo) + "\nDisponibilidade: " + str(self.__disponibilidade) + 
              "\nEstoque: " + str(self.__estoque))