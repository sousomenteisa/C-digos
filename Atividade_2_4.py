#Variaveis locais e globais
#É interessante evitar variáveis globais 

#Faça um código com uma variável local 
#Faça um código com uma variáel global
#Faça um terceiro código com duas ou mais variáveis, mas pelo menos uma local e uma global 

#Código_1: Performance rotina
#Um programa de lista de afazeres

def criar_lista_1(*inserir_tarefas):
    lista_tarefas = []
    lista_tarefas.append(inserir_tarefas)
    return lista_tarefas

print(criar_lista_1("inserir_aqui"))

def criar_lista_2(*inserir_tarefas):
    lista_tarefas = []
    lista_tarefas.append(inserir_tarefas)
    return lista_tarefas

inerir_tarefas = input("Digite suas tarefas separadas por vírgula: ")
print(criar_lista_2("inserir_aqui"))


def criar_lista_3(*inserir_dados):
    dados_num = []
    dados_str = []
    if inserir_dados == int:
        dados_num.append(inserir_dados)
    if inserir_dados == str:
        dados_str.append(inserir_dados)
    return dados_num and dados_str

print(criar_lista_3(5, "sete", 8, 9, "dez"))



    
    











    