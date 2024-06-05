class Produto:
    def __init__(self, tipo_produto, codigo_produto, descricao_produto):
        self.__tipoproduto = tipo_produto
        self.__codigoproduto = codigo_produto
        self.__descricaoproduto = descricao_produto

    def get_tipo(self):
        return self.__tipoproduto
    
    def set_tipo(self, novoTipo):
        if novoTipo == "":
            raise ValueError("Novo tipo não pode ser vazio")
        else:
            self.__tipoproduto = novoTipo
    
    def get_codigo(self):
        return self.__codigoproduto
    
    def set_codigo(self, novoCodigo):
        if novoCodigo <= 0:
            raise ValueError("Código não pode ser zero ou negativo")
        elif type(novoCodigo) != int:
            raise ValueError("Código deve ser um número inteiro")
        else:
            self.__codigoproduto = novoCodigo

    def get_descricao(self):
        return self.__descricaoproduto
    
    def set_descricao(self, novaDescricao):
        self.__descricaoproduto = novaDescricao

    def imprime_produto(self):
        print("Tipo Produto: " + str(self.__tipoproduto) + "\nCódigo Produto: "
               + str(self.__codigoproduto) + "\nDescrição Produto: " + 
               str(self.__descricaoproduto))
