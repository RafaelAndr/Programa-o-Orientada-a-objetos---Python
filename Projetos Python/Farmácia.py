import pickle

class TpFarma:
    def __init__(self, nome, preco, q_estoque, categoria):
        self.nome = nome
        self.preco = preco
        self.q_estoque = q_estoque
        self.categoria = categoria

def incluir():
    with open("Farmacos.pickle", "rb") as arquivo:
        farmacos = pickle.load(arquivo)

    while True:
        nome = input("Nome: ")
        if nome in farmacos:
            print("Este Medicamento já existe, escolha um diferente.")
        else:
            break

    preco = float(input("Preço: "))
    q_estoque = int(input("Estoque: "))
    categoria = input("Qual a categoria? ")

    farmaco = TpFarma(nome, preco, q_estoque, categoria)
    farmacos[nome] = farmaco

    with open("Farmacos.pickle", "wb") as arquivo:
        pickle.dump(farmacos, arquivo)

    resposta = input("\nNova inclusão? S/N ")
    if resposta.upper() != "S":
        print("Registro armazenado com sucesso!")

def excluir():
    with open("Farmacos.pickle", "rb") as arquivo:
        farmacos = pickle.load(arquivo)

    nome = input("Qual Medicamento deseja excluir? ")
    if nome in farmacos:
        del farmacos[nome]
        with open("Farmacos.pickle", "wb") as arquivo:
            pickle.dump(farmacos, arquivo)
        print(">>> Exclusão efetuada com sucesso! <<<")
    else:
        print("Medicamento inexistente!")

def alterar():
    with open("Farmacos.pickle", "rb") as arquivo:
        farmacos = pickle.load(arquivo)

    nome = input("Qual farmaco? ")
    if nome in farmacos:
        farmaco = farmacos[nome]

        print(f"Nome: {farmaco.nome}")
        print(f"Valor: {farmaco.preco}")
        print(f"Estoque: {farmaco.q_estoque}")
        print(f"Categoria: {farmaco.categoria}")

        sub_opcao = input("\nOpções de alteração:\n"
                          "P - Alterar Preço\n"
                          "Q - Alterar Quantidade\n"
                          "C - Alterar Categoria\n"
                          "S - Sair\n"
                          "Escolha uma opção: ")
        sub_opcao = sub_opcao.upper()

        if sub_opcao == "P":
            preco = float(input("Qual o novo preço? "))
            farmaco.preco = preco
        elif sub_opcao == "Q":
            q_estoque = int(input("Qual a nova quantidade? "))
            farmaco.q_estoque = q_estoque
        elif sub_opcao == "C":
            categoria = input("Qual a nova categoria? ")
            farmaco.categoria = categoria
        elif sub_opcao == "S":
            print("Saindo do submenu de alteração.")
        else:
            print("Opção inválida.")

        with open("Farmacos.pickle", "wb") as arquivo:
            pickle.dump(farmacos, arquivo)

        print(">>> Alteração efetuada com sucesso! <<<")
    else:
        print("Registro inexistente!")

def consultar():
    with open("Farmacos.pickle", "rb") as arquivo:
        farmacos = pickle.load(arquivo)

    nome = input("Qual farmaco? ")
    if nome in farmacos:
        farmaco = farmacos[nome]
        print(f"Nome: {farmaco.nome}")
        print(f"Valor: {farmaco.preco}")
        print(f"Estoque: {farmaco.q_estoque}")
        print(f"Categoria: {farmaco.categoria}")
    else:
        print("Registro inexistente!")

def consulta_categoria():
    with open("Farmacos.pickle", "rb") as arquivo:
        farmacos = pickle.load(arquivo)

    categoria = input("Qual a categoria? ")
    print("\n")
    achou = False

    for farmaco in farmacos.values():
        if farmaco.categoria == categoria:
            print(f"Nome: {farmaco.nome}")
            print(f"Valor: {farmaco.preco}")
            print(f"Estoque: {farmaco.q_estoque}")
            print(f"Categoria: {farmaco.categoria}")
            print("***\n\n")
            achou = True

    if not achou:
        print("Nenhum medicamento encontrado nessa categoria.")

def listar_todos():
    with open("Farmacos.pickle", "rb") as arquivo:
        farmacos = pickle.load(arquivo)

    for farmaco in farmacos.values():
        print(f"Nome: {farmaco.nome}")
        print(f"Valor: {farmaco.preco}")
        print(f"Estoque: {farmaco.q_estoque}")
        print(f"Categoria: {farmaco.categoria}")
        print("***\n\n")

def main():
    try:
        with open("Farmacos.pickle", "rb") as arquivo:
            farmacos = pickle.load(arquivo)
    except FileNotFoundError:
        farmacos = {}

    opcao = ""
    while opcao != "S":
        print("\n\n> > > Pague Pouco < < < \n\n")
        print("O que deseja fazer?\n")
        print("I - Incluir")
        print("E - Excluir")
        print("A - Alterar")
        print("C - Consultar")
        print("X - ConsultaCategoria")
        print("T - Listar Todos")
        print("S - Sair\n")

        opcao = input("Escolha uma opção: ").upper()

        if opcao == "I":
            incluir()
        elif opcao == "E":
            excluir()
        elif opcao == "A":
            alterar()
        elif opcao == "C":
            consultar()
        elif opcao == "X":
            consulta_categoria()
        elif opcao == "T":
            listar_todos()

if __name__ == "__main__":
    main()
