from produto import Produto

class Impressora(Produto):
    def __init__(self, tipo_produto, codigo_produto, descricao_produto, modelo, tipo_impressora):
        super().__init__(tipo_produto, codigo_produto, descricao_produto)
        self.__tipo_impressora = tipo_impressora  # Changed the attribute name
        self.__modelo = modelo  # Changed the attribute name
        self.__disponibilidade = 0
        self.__estoque = True

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):  # Changed the parameter name
        self.__modelo = novo_modelo

    def get_tipo_impressora(self):  # Changed the method name to follow PEP8 conventions
        return self.__tipo_impressora

    def set_tipo_impressora(self, novo_tipo):  # Changed the method name to follow PEP8 conventions
        self.__tipo_impressora = novo_tipo

    def get_disponibilidade(self):
        return self.__disponibilidade

    def get_estoque(self):
        return self.__estoque  # Simplified the method to return the attribute directly

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
        print("Modelo: " + self.__modelo + "\nDisponibilidade: " + str(self.__disponibilidade) +  # Convert to str
              "\nEstoque: " + str(self.__estoque))  # Convert to str
