#print(): Exibe dados na tela ou no terminal.
#input(): Captura uma entrada de texto digitada pelo usuário.
#type(): Retorna o tipo de dado de uma variável.
#int(): Converte um valor para número inteiro.
#float(): Converte um valor para número decimal.
#str(): Converte qualquer valor para texto (string).
#bool(): Converte um valor para booleano (True ou False).
#list(): Converte uma sequência em uma lista.
#len(): Retorna o tamanho/quantidade de itens de uma string, lista ou coleção.
#sum(): Soma todos os elementos numéricos de uma lista ou sequência.
#max(): Retorna o maior valor de uma coleção.
#min(): Retorna o menor valor de uma coleção.
#abs(): Retorna o valor absoluto (positivo) de um número.
#round(): Arredonda um número flutuante para um número fixo de casas decimais.
#range(): Gera uma sequência de números inteiros (muito usada em laços for).
#enumerate(): Retorna os itens de uma lista acompanhados de seus respectivos índices.
#Escolha 5 funções embutidas.
#Tente criar com elas uma estrutura sequencial.
#Explique para que tipo de contexto esse código poderia ser aplicado.

categoria = input("Digite a categoria de gasto (Alimentação, transporte, utilidades, assinaturas, delivery, outros): ")
valor_gasto_mensal = int(input("qual foi o seu gasto mensal dentro dessa categoria?"))

gasto_em_alimentacao = []
gasto_em_transporte = []
gasto_em_utilidades = []
gasto_em_assinaturas = []
gasto_em_delivery = []
gasto_em_outros = []


if categoria == "Alimentacao":
    gasto_em_alimentacao.append(int(valor_gasto_mensal))
elif categoria == "transporte":
    gasto_em_transporte.append(float(valor_gasto_mensal))
elif categoria == "utilidades":
    gasto_em_utilidades.append(float(valor_gasto_mensal))
elif categoria == "assinaturas":
    gasto_em_assinaturas.append(float(valor_gasto_mensal))
elif categoria == "delivery":
    gasto_em_delivery.append(float(valor_gasto_mensal))
else:
    gasto_em_outros.append(float(valor_gasto_mensal))   

print(f"Gasto em alimentação: {gasto_em_alimentacao}")
print(f"Gasto em transporte: {gasto_em_transporte}")
print(f"Gasto em utilidades: {gasto_em_utilidades}")
print(f"Gasto em assinaturas: {gasto_em_assinaturas}")
print(f"Gasto em delivery: {gasto_em_delivery}")
print(f"Gasto em outros: {gasto_em_outros}")

    
