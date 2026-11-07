import pandas as pd

#Ler o arquivo CSV
caminho_csv = "Aula 4/boticario_products.csv"
df = pd.read_csv(caminho_csv)

#Mostrar as 5 primeiras linhas
print("=== Primeiras linhas ===")
print((df.head))

#2. Informações gerais do DataFrame 
print("\n=== Formato (Linhas, colunas) ===")
print(df.shape)

print("\n === Nomes das colunas ===")
print(df.columns.tolist())

print("\n=== Tipos de dados ===")
print(df.dtypes)

## 3. Percorrer as colunas
print("\n=== Percorrendo colunas ===")
for coluna in df.columns:
    print(f"- {coluna}: {df[coluna].dtype}")

# Percorrer colunas e mostrar um valor de exemplo
for coluna in df.columns:
    print(f"{coluna} --> exemplo: {df[coluna].iloc[0]}")

# Selecionar colunas de interesse
colunas_interesse = ["name", "regular_price", "promotional_price", "product_line"]
df_resumo = df[colunas_interesse]
print("\n=== Colunas selecionadas ===")
print(df_resumo.head())

#quando não tiver a biblioteca instalada: colocar pip3  install pandas

#Produtos com produção ativa
df_promocao = df[df["promotion_active"] == True]
print(f"\n=== Produtos em promoção: {len(df_promocao)} linhas ===")
print(df_promocao[["name", "promotional_price", "discount_percentage"]].head())

## Produtos de Perfumaria com desconto acima de 30%
df_perfumaria = df[
    (df["normalized_category"] == "Perfumaria") &
    (df["discount_percentage"] > 30)
]

print(f"\n foram encontrador {len(df_perfumaria)} produtos ===")
print(df_perfumaria[["name", "discount_percentage"]].head())

#6. Adicionar novas colunas 
df["economia_reais"] = df["regular_price"] - df["promotional_price"]

df["em_promocao"] = df["promotion_active"].map({True: "Sim", False: "Não"})

df["faixa_preco"] = pd.cut(
    df["promotional_price"], #pega a coluna 
    bins=[0, 50, 100, 200, float("inf")], #faz cortes de intervalo definidos por você
    labels=["Até R$ 50", "R$ 50-100", "R$ 100-200", "Acima de R$ 200",]
) #criando a coluna faixa de preço

print("\n=== Novas colunas criadas ===")
print(df[["name", "regular_price", "promotional_price", "economia_reais", "em_promocao", "faixa_preco"]].head())

#7. Outras manipulações básicas
#Ordenar por maior desconto
df_ordenado = df.sort_values("discount_percentage", ascending=False)
print("\n=== Top 5 maiores descontos ===")
print(df_ordenado[["name", "discount_percentage"]].head())

# Contar produtos por categoria 
print("\n=== Quantidade por categoria ===")
print(df["normalized_category"].value_counts().head())

#Média de preço por linha de produto 
print("\n === Preço médio promocional por linha ===")
print(df.groupby("product_line")["promotional_price"].mean().sort_values(ascending=False).head())

#Renomear coluna
df = df.rename(columns={"name": "nome_produto"})
print("\n=== Coluna renomeada ===")
print(df[["nome_produto", "product_line"]].head(3))

## Remover duplicatas(se houver)
print(f"\n=== Linhas antes de remover duplicatas: {len(df)} ===")
df = df.drop_duplicates(subset=["code"])
print(f"=== Linhas depois: {len(df)} ===")