class Vehicle:
    def __init__(self, nome, velocidade_max, dist):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.dist = dist

    def dados_carro(self):
        print(f'o carro {self.nome}, velocidade: {self.velocidade_max}, distancia: {self.dist}')

Vehicle_1 = Vehicle("Tesla Model S", 250, 40)

Vehicle_1.dados_carro()
