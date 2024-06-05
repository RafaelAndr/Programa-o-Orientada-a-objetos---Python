class Veiculo:
	def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo):
		self._placaVeiculo = placaveiculo
		self._fabricanteVeiculo = fabricanteveiculo
		self._numeroRodas = numerorodas
		self._tipoVeiculo = tipoveiculo

	def imprime(self):
		print("Placa do veiculo: " + self._placaVeiculo + 
	"\nFabricante do veiculo: " + self._fabricanteVeiculo + "\nNumero de rodas: " 
	+ str(self._numeroRodas) + "\nTipo de veiculo " + self._tipoVeiculo)
    
	def getFabricanteVeiculo(self):
		return self._fabricanteVeiculo

	def setFabricanteVeiculo(self, fabricanteveiculo):
		if len(fabricanteveiculo) == 0:
			print ("Fabricante de veiculo vazio")
		else:
			self._fabricanteVeiculo = fabricanteveiculo

	def getPlacaVeiculo(self):
		return self._placaVeiculo

	def setPlacaVeiculo(self, placaveiculo):
		if len(placaveiculo) == 0:
			print ("Placa de veiculo vazio")
		else:
			self._placaVeiculo = placaveiculo

	def getNumeroRodas(self):
		return self._numeroRodas

	def setNumeroRodas(self, numerorodas):
		if numerorodas <= 0:
			print ("Numero de rodas invalido")
		else:
			self._numeroRodas = numerorodas

	def getTipoVeiculo(self):
		return self._tipoVeiculo

	def setTipoVeiculo(self, tipoveiculo):
		if len(tipoveiculo) == 0:
			print ("Tipo de veiculo vazio")
		else:
			self._tipoVeiculo = tipoveiculo

class Carro(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, portas):
        super().__init__( placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__portas = portas

    def getPortas(self):
        return self.__portas
    
    def setPortas(self, portas):
        if portas <= 0:
            print("Número de portas Inválido")
        else:
            self.__portas = portas
    
    def imprimeCarro(self):
        super().imprime()
        print("Portas: " + str(self.__portas))

class Moto(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, cilindrada):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__cilindradas = cilindrada

    def getCilindradas(self):
        return self.__cilindradas
    
    def setCilindradas(self, cilindradas):
        if cilindradas <= 0:
            print("Número de cilindradas Inválido")
        else:
            self.__cilindradas = cilindradas

    def imprimeMoto(self):
        super().imprime()
        print("Cilindradas: " + str(self.__cilindradas))

class Bicicleta(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, marchas):
        super().__init__( placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__marchas = marchas

    def getMarchas(self):
        return self.__marchas
    
    def setMarchas(self, marchas):
        if marchas <= 0:
            print("Número de marchas Inválido")
        else:
            self.__marchas = marchas

    def imprimeBicicleta(self):
        super().imprime()
        print("Marchas: " + str(self.__marchas))

class Frota:
    def __init__(self):
        self.__frota = []

    def inserirVeiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__frota.append(veiculo)
        else:
            print("Erro: o objeto passado nao é do tipo Veiculo.")

    def removerVeiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__frota.remove(veiculo)
        else:
            print("Erro: o objeto passado nao é do tipo Veiculo.")
    
    def localizarVeiculo(self, placa):
        for veiculo in self.__frota:
            if veiculo.getPlacaVeiculo() == placa:
                veiculo.imprime()
    
    def listarVeiculos(self):
        for veiculo in self.__frota:
            if (isinstance(veiculo, Carro)):
                print("------------")
                print("Tipo: Carro")
                veiculo.imprimeCarro()
            if (isinstance(veiculo, Moto)):
                print("------------")
                print("Tipo: Moto")
                veiculo.imprimeMoto()
            if (isinstance(veiculo, Bicicleta)):
                print("------------")
                print("Tipo: Bicicleta")
                veiculo.imprimeBicicleta()

def main():
    frota = Frota()
    carro1 = Carro("QKN-2039", "HONDA", 4, "CIVIC", 4)
    moto1 = Moto("QKY-4738", "YAMAHA", 2, "HORNET", 600)
    bicileta1 = Bicicleta("QJA-3847", "CALOI", 2, "EXPLORER", 21)
    frota.inserirVeiculo(carro1)
    frota.inserirVeiculo(moto1)
    frota.inserirVeiculo(bicileta1)
    frota.removerVeiculo(carro1)
    frota.listarVeiculos()

if __name__ == "__main__":
    main()