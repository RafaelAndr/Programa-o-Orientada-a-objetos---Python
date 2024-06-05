from impressora import Impressora

def main():
    impressora = Impressora("Eletronico", 25353, "Barato", "Boa", "samsung")
    impressora.set_tipo("Digital")
    print(impressora.get_tipo())
    impressora.set_codigo(24352)
    print(impressora.get_codigo())
    impressora.set_descricao("Caro")
    print(impressora.get_descricao())
    impressora.set_tipoimpressora("Ruim")
    print(impressora.get_tipoimpressora())
    impressora.set_modelo("Samsung")
    print(impressora.get_modelo())
 
    try:
        impressora.aumenta_estoque(2)
    except ValueError as erro:
        print(erro)

    try:
        impressora.diminui_estoque(4)
    except ValueError as erro:
        print(erro)

if __name__ == "__main__":
    main()