import datetime

class Veiculo:
    def __init__(self, placa):
        self.placa = placa
        self.hora_entrada = None
        self.hora_saida = None
        self.valor_pago = None

class Estacionamento:
    def __init__(self):
        self.vagas = ['LIVRE'] * 30
        self.veiculos = []

    def entrada_veiculo(self, placa):
        if 'LIVRE' in self.vagas:
            vaga = self.vagas.index('LIVRE')
            self.vagas[vaga] = placa
            veiculo = Veiculo(placa)
            veiculo.hora_entrada = datetime.datetime.now()
            self.veiculos.append(veiculo)
            print(f"Veículo com placa {placa} estacionado na vaga {vaga + 1}.")
        else:
            print("Não há vagas disponíveis no momento.")

    def saida_veiculo(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa and veiculo.hora_saida is None:
                vaga = self.vagas.index(placa)
                veiculo.hora_saida = datetime.datetime.now()
                tempo_estacionado = veiculo.hora_saida - veiculo.hora_entrada
                valor_pago = self.calcular_valor_pago(tempo_estacionado.total_seconds() / 3600)
                veiculo.valor_pago = valor_pago
                self.vagas[vaga] = 'LIVRE'
                print(f"Veículo com placa {placa} saiu da vaga {vaga + 1}.")
                print(f"Tempo estacionado: {tempo_estacionado}")
                print(f"Valor pago: R${valor_pago:.2f}")
                self.registrar_saida_em_arquivo(veiculo)
                return
        print(f"Veículo com placa {placa} não encontrado ou já saiu do estacionamento.")

    def exibir_vagas(self):
        print("Estado das vagas:")
        for i, vaga in enumerate(self.vagas):
            if vaga == 'LIVRE':
                print(f"Vaga {i + 1}: LIVRE")
            else:
                print(f"Vaga {i + 1}: Ocupada (Placa: {vaga})")

    def calcular_valor_pago(self, horas):
        valor_hora = 10.0  # Valor por hora de estacionamento
        return valor_hora * horas

    def registrar_saida_em_arquivo(self, veiculo):
        arquivo = open("relatorio_estacionamento.txt", "a")
        arquivo.write(f"Placa: {veiculo.placa}\n")
        arquivo.write(f"Hora de entrada: {veiculo.hora_entrada}\n")
        arquivo.write(f"Hora de saída: {veiculo.hora_saida}\n")
        arquivo.write(f"Valor pago: R${veiculo.valor_pago:.2f}\n")
        arquivo.write("--------\n")
        arquivo.close()

# Exemplo de uso
estacionamento = Estacionamento()

while True:
    print("----- Estacionamento -----")
    print("1. Entrada de veículo")
    print("2. Saída de veículo")
    print("3. Exibir vagas")
    print("4. Exibir relatório")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        placa = input("Digite a placa do veículo: ")
        estacionamento.entrada_veiculo(placa)
    elif opcao == "2":
        placa = input("Digite a placa do veículo: ")
        estacionamento.saida_veiculo(placa)
    elif opcao == "3":
        estacionamento.exibir_vagas()
    elif opcao == "4":
        arquivo = open("relatorio_estacionamento.txt", "r")
        print("----- Relatório do Estacionamento -----")
        print(arquivo.read())
        arquivo.close()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")
