VZonda = []

class TpRegMoto:
    def __init__(self, nome, modelo, placa, defeito, status='0', preco=0):
        self.nome = nome
        self.modelo = modelo
        self.placa = placa
        self.defeito = defeito
        self.status = status
        self.preco = preco

def solicitar_servico():
    while True:
        print("\n\n >>> Motos Zonda <<< \n\n")
        nome = input("Qual o nome do cliente? ")
        modelo = input("Qual o modelo da moto? ")
        placa = input("Qual a placa da moto? ")
        defeito = input("Qual o defeito da moto? ")

        moto = TpRegMoto(nome, modelo, placa, defeito)
        VZonda.append(moto)

        sair = input("\n\n Deseja inserir novo serviço? S|N ")
        if sair.upper() != "S":
            print("Registro armazenado com sucesso!")
            break

def iniciar_servico():
    placa = input("Placa da moto para iniciar serviço: ")
    pos = -1

    for i, moto in enumerate(VZonda):
        if moto.placa == placa:
            pos = i
            break

    if pos == -1:
        print("Moto não cadastrada!")
    else:
        moto = VZonda[pos]
        print(f"\n Cliente {pos+1}: {moto.nome}")
        print(f" Modelo: {moto.modelo}")
        print(f" Placa: {moto.placa}")
        print(f" Defeito: {moto.defeito}")
        moto.status = '1'
        print(f" Status: {moto.status}")
        if moto.preco == 0:
            print(" Preço: NÃO DEFINIDO")
        else:
            print(f" Preço: {moto.preco:.2f}")

def remover_solicitacao():
    pass

def consultar_solicitacoes():
    print("\n\n >>> Motos Zonda <<< \n\n")
    if len(VZonda) == 0:
        print("Não há serviços cadastrados.")
    else:
        for i, moto in enumerate(VZonda):
            print(f"\n Cliente {i+1}: {moto.nome}")
            print(f" Modelo: {moto.modelo}")
            print(f" Placa: {moto.placa}")
            print(f" Defeito: {moto.defeito}")
            print(f" Status: {moto.status}")
            if moto.preco == 0:
                print(" Preço: NÃO DEFINIDO")
            else:
                print(f" Preço: {moto.preco:.2f}")
            print("---------------------\n\n")

def concluir_servico():
    pass

def encerrar_expediente():
    pass

def main():
    while True:
        print("\n\n >>> Motos Zonda <<< \n\n")
        print("1 - Solicitar Serviço")
        print("2 - Iniciar Serviço")
        print("3 - Remover Solicitação")
        print("4 - Consultar Solicitações")
        print("5 - Concluir Serviço")
        print("6 - Encerrar Expediente")
        print("7 - Sair\n")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            solicitar_servico()
        elif opcao == 2:
            iniciar_servico()
        elif opcao == 3:
            remover_solicitacao()
        elif opcao == 4:
            consultar_solicitacoes()
        elif opcao == 5:
            concluir_servico()
        elif opcao == 6:
            encerrar_expediente()
        elif opcao == 7:
            break

if __name__ == "__main__":
    main()
