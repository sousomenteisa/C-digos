#Listas em Python
lista_vazia = []
lista_numeros = [10, 20, 30, 40, 50] #hardcoded
lista_mista = [1, "Python", 3.14, True]
#print(lista_numeros[0])
#print(lista_mista[3])
lista_numeros.append(60)
#print(lista_numeros)
lista_numeros.remove(20)
#print(lista_numeros)

#Percorrendo listas com for
#for i in lista_mista:
    #print(i)

#Tuplas
tupla_exemplo = (10, 20, 30)
tupla_mista = (1, "Python", 3.14)
#print(tupla_exemplo[1])
#print(tupla_mista[2])

dados_pessoais = [("Isabel", 25, "Pedagogia"), ("Henrique", 25, "Letras"), ("Mateus", 30, "Medicina")]
for pessoa in dados_pessoais:
    nome, idade, curso = pessoa
    #print(f"A(O) estudante {nome}, tem {idade} e está cursando o curso de {curso}")

#Transformando tupla em lista
alunos = ("Arthur", "Maria Alice", "Helena", "Joaquin", "Felipe")
alunos_lista = list(alunos)
#print(alunos_lista)

#Dicinarios e conjuntos

aluno = {
    "nome": "Nathy",
    "idade": 26,
    "Curso": "Publicidade e Propaganda"
}

#print(aluno["nome"])
#print(aluno["idade"])
#print(aluno["Curso"])

aluno["faltas"] = 25

#print(aluno["faltas"])
aluno["nivel"] = "PCPT2-2"
#print(aluno["nivel"])

#for chave, valor in aluno.items():
    #print(chave, valor)

#Conjuntos
frutas = {"maçã", "banana", "abacaxi"}
#adicionando ou removendo
frutas.add("melancia")
#print(frutas)
frutas.add("morango")
frutas.add("uva")
#print(frutas)
frutas.discard("melancia")
#print(frutas)
#Conjuntos sao ideiais para remover dados duplicados e os ordenar

#[]brackets 
#()parentheses(plural) ou parenthesis (singular)
#{}braces

numeros = set([1, 2, 2, 3])
#print(numeros)

#operações matemáticas de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
#print(a | b) #Uniao -- > {1, 2, 3, 4, 5}
#print(a & b) #Interseção --> {3}
#print(a - b) #diferença --> {1, 2}
#print(a ^ b) #diferença simétrica --> {1, 2, 3, 4, 5}

#Dicionário base para os testes.
d = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "São Paulo",
    "profissao": "Dev"
}

#Testando os métodos
#print(d["nome"])
d["idade"] = 31
#print(d["idade"])
d["cidade"] = "Curitiba"
#print(d["cidade"])
idade = d.get("idade", 0)
#print("idade:", idade)

#--TESTANDO OS MÉTODOS---
# .get(chave, valor_padrao) --> Busca "altura", mas como não existe, retorna o
altura = d.get("altura", "Sem valor")
#print("altura:", altura)

chaves = d.keys()
#print(chaves)

valores = d.values()
#print(valores)

items = d.items()
#print(items)

#aqui ele retorna a chave, mas modificar o dicionário
pop_example = d.pop("cidade")
#print(pop_example)
#print(d)

#atualiza ou adiciona pares
d.update({"empresa": "Ebanx"})
#print(d)

#Remove tudo
d.clear()
#print(d)

#Faz uma cópia
copia = d.copy()
#print(copia)

#conjunto base para os testes
s = {"maçã", "banana", "uva"}
s1 = {"maçã", "banana", "uva"}
s2 = {"uva", "laranja", "abacaxi"}
s3 = {"laranja", "abacaxi"}

s.add("melancia")
#print(s)

#s.remove("banana")
#print(s)

s.discard("pera")
#print(s)

#s.pop()
#print(s)

s.clear()
#print(s)

#s1.union(s2)
#print(s1)

#intersecao
em_comum = s1.intersection(s2)
em_comum_v2 = s1 & s2
#print(em_comum)


#difference
diferenca = s1.difference(s2)
diferenca_v2 = s1 - s2
#print(s1.difference(s2))

#subset
curiosidade_1 = s1.issubset(s2)
print(curiosidade_1)
curiosidade_2 = s2.issubset(s1)
print(curiosidade_2)
curiosidade_3 = s3.issubset(s2)
print(curiosidade_3)

#superset
curiosidade_4 = s1.issuperset(s2)
print(curiosidade_4)
curiosidade_5 = s2.issuperset(s3)
print(curiosidade_5)

#disjoint(nada em comum)
curiosidade_6 = s.isdisjoint(s2)
print(curiosidade_6)

#usando *args para somar qualquer quantidade de números
def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(10, 20))
print(somar_tudo(5, 10, 15, 20))


#Usando **kwargs para cadastrar um perfil de dados flexíveis
def criar_perfil(nome, **detalhes):
    print(f"usuário: {nome}")

    for chave, valor in detalhes.items(): #items percorre chave
        print(f"- {chave}: {valor}")


criar_perfil("Ana", idade=25, curso="Python", ativo=True)
      
#%%
def calcular_desconto(preco, percentual):
    # Print de verificação: checar os valores que entraram 
    print(f"Entrada --> preço: {preco}, percentual: {percentual}")
    desconto = preco * percentual / 100
    print(f"Valor calculado do desconto: {desconto}")
    return preco - desconto
#chama a função esperando 10% de desconto sobre 100

resultado = calcular_desconto(100, 10)
print(f"Resultado Final: {resultado}")





