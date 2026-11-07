def criar_lista_3(*inserir_dados):
    dados_num = []
    dados_str = []
    if inserir_dados == int:
        dados_num.append(inserir_dados)
        return dados_num
    if inserir_dados == str:
        dados_str.append(inserir_dados)
        return dados_str

print(criar_lista_3(5, "sete", 8, 9, "dez"))



def criar_lista_3(*inserir_dados):

    dados_num = []
    dados_str = []

    for dado in inserir_dados:

        if isinstance(dado, int):
            dados_num.append(dado)

        if isinstance(dado, str):
            dados_str.append(dado)

    return dados_num, dados_str


print(criar_lista_3(5, "sete", 8, 9, "dez"))