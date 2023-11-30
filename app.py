class veiculo: 
    
    def __init__(self,eixos):

        self.eixos = eixos

    def pegadio(self): raise NotImplementedError ("escolha o tamanho do veiculo")

class VeiculoPasseio(veiculo):
    
    def __init__(self, eixos):
        super().__init__(eixos)
        self.tipo = "Veiculo de Passeio"

    def pegadio(self):
        return self.eixos*10

class VeiculoPesado(veiculo):

    def __init__(self, eixos):
        super().__init__(eixos)
        self.tipo = "Veiculo Pessado"
    
    def pegadio(self):
        if self.eixos <= 5:
            return self.eixos * 25

        if self.eixos > 5:

            eixos_extras = self.eixos-5
            valor_max = 5 * 25
            valor_eixo_extra = eixos_extras * 35

            return valor_max + valor_eixo_extra

class Motocicleta(veiculo):

    def __init__(self, eixos):
        super().__init__(eixos)
        self.tipo = "Motocicleta"

    def pegadio(self):
        return 5

#Inicializando os veiculos: 

c1 = VeiculoPasseio(2) # veiculo de passseio com 2 eixos
c2 = VeiculoPasseio(3) # veiculo de passseio com 3 eixos
c3 = VeiculoPasseio(4) # veiculo de passseio com 4 eixos
c4 = VeiculoPesado(5) # Veiculo pessado com 5 eixos
c5 = VeiculoPesado(6) # Veiculo pessado com 6 eixos
c6 = VeiculoPesado(7) # Veiculo pessado com 7 eixos
m1 = Motocicleta(1) # Moto com 1 eixo


def calcular_valor_pedagio(veiculo):
    tarifa = veiculo.pegadio()
    print(f"------------------------------")
    print(f"Tipo de veiculo: {veiculo.tipo}\nNumero de eixos: {veiculo.eixos}\nValor Pedagio: {tarifa} reais")
    print("------------------------------\n")

calcular_valor_pedagio(c1)
calcular_valor_pedagio(c2)
calcular_valor_pedagio(c3)
calcular_valor_pedagio(c4)
calcular_valor_pedagio(c5)
calcular_valor_pedagio(c6)
calcular_valor_pedagio(m1)