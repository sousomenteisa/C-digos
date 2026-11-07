import matplotlib.pyplot as plt
# 1. Dados simples do cotidiano
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']
cafes_tomados = [2, 4, 3, 5, 1]

# 2. Criando o gráfico 
plt.plot(dias, cafes_tomados, marker='o')

# 3. Nomeando cada pedaço que você explicou 
plt.title('Consumo de café ao longo da semana') #Manchete
plt.xlabel('Dias da Semana') #Eixo horizontal (X)
plt.ylabel("Quantidade de xícaras") #Eixo vertical (Y)

#4. Exibindo na tela
plt.show()