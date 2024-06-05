from produto import Produto

def main():
    produto = Produto("Móvel", 23733, "Barato")
    try:
        produto.set_tipo("Celular")
    except ValueError as erro:
        print(erro)
    print(produto.get_tipo())
    try:
        produto.set_codigo(12203)
    except ValueError as erro:
        print(erro)
    print(produto.get_codigo())
    produto.set_descricao("caro")
    print(produto.get_descricao())


if __name__ == "__main__":
    main()