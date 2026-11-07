
def registro(venda_registro):
        numero_venda = int(venda_registro)
        lista_de_vendas_acumuladas = []
        for i in range(numero_venda):
            venda_realizada = int(input("registre sua venda aqui"))
            lista_de_vendas_acumuladas.append(venda_realizada)
        return lista_de_vendas_acumuladas

def levantamento_vendas(lista_vendas):
      numero_vendas = len(lista_vendas)
      faturamento_bruto = sum(lista_vendas)
      ticket_medio = faturamento_bruto/numero_vendas
      return f"foram realizadas um total de {numero_vendas}, com um faturamento bruto de {faturamento_bruto} e tiket médio de {ticket_medio}"

registro_vendas = input("Bem vindo ao sistema de registro de vendas, você deve registrar a quantidade de vendas realizadas")
registro_vendas_lote_1 = registro(registro_vendas) #você deve registrar a quantidade de vendas realizadas
vendas_realizadas = levantamento_vendas(registro_vendas_lote_1)
print(vendas_realizadas)









    