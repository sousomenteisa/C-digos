def cadastramento_de_produtos(insira_o_produto):
    produtos = []
    produtos.append(insira_o_produto)

    relacao_produtos = {}

    for produto in produtos:
        relacao_produtos[produto] = produtos.index(produto)
        return relacao_produtos

protocolar = cadastramento_de_produtos("banana")

print(protocolar)
