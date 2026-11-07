#variavel local
def saudacao():
    nome = input("Digite seu nome aqui")
    return (f"olá, {nome}!")

print (saudacao())

 
#variavel global
def saudacao(idade):
    return (f"Olá, {idade}! Você tem {idade} anos")
nome = "Isa"
print(f"Meu nome é {nome}")
print(saudacao(26))
