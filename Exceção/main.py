from conta import Conta

conta1 = Conta("Robson", 1234500)

conta1.deposito(1000)
conta1.imprimeConta()
successful = False
tentativas = 0

while (not successful) and (tentativas < 3):
    try:
        conta1.saque(1500)
        successful = True
    except ValueError as erro:
        print(erro)
        tentativas += 1

if not successful:
    print("Nao foi possivel realizar o saque")
    tentativas = 0

while (not successful) and (tentativas < 3):
    try:
        conta1.saque(580)
        successful = True
    except ValueError as erro:
        print(erro)
        tentativas += 1

flagDeposito = False
tentD = 0
while (not flagDeposito) and (tentD < 3):
    try:
        conta1.deposito(-580)
        successful = True
    except ValueError as erro:
        print(erro)
        tentD += 1

if not successful:
    print("Nao foi possivel realizar o saque")

try:
    conta1.setNomeCorrentista("")
    conta1.setNumeroConta("4444")

except:
    print("Erro")

conta1.imprimeConta()

