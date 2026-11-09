"""
DESAFIO — Aula 4: Pandas com dados do Boticário
================================================

Você é analista de uma loja e precisa responder perguntas sobre o catálogo
de produtos usando o arquivo `boticario_products.csv`.

Use apenas o que vimos na Aula_4.py:
  - pd.read_csv, .head(), .shape, .columns, .dtypes, .iloc
  - Seleção de colunas: df[["col1", "col2"]]
  - Filtros com condições: df[df["col"] == valor] e operador &
  - Novas colunas: cálculos, .map() e pd.cut()
  - .sort_values(), .value_counts(), .groupby()
  - .rename() e .drop_duplicates()

Regras:
  1. Cada tarefa deve ter seu próprio bloco de código.
  2. Use print() com um título claro antes de cada resposta.
  3. Não altere o arquivo CSV original.
  4. Bônus: tente resolver sem olhar a Aula_4.py — consulte só se travar!

Pontuação sugerida: 10 pts (Tarefas 1–8) + 2 pts bônus (Desafio Final)
"""

import pandas as pd

# ── Carregamento (já feito para você) ────────────────────────────────────────
df = pd.read_csv("boticario_products.csv")


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 1 — Conhecendo os dados (1 pt)
# ═══════════════════════════════════════════════════════════════════════════
# Imprima:
#   a) As 3 primeiras linhas do DataFrame
#   b) Quantas linhas e colunas existem
#   c) A lista com os nomes de TODAS as colunas
#   d) Os tipos de dados de cada coluna

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 2 — Seleção e filtro (1,5 pts)
# ═══════════════════════════════════════════════════════════════════════════
# a) Crie um DataFrame `df_resumo` apenas com as colunas:
#    "name", "normalized_category", "regular_price", "promotional_price"
#    Mostre as 5 primeiras linhas.
#
# b) Filtre produtos da categoria "Corpo e Banho" que estão em promoção
#    (promotion_active == True). Imprima quantas linhas foram encontradas.

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 3 — Criando colunas (1,5 pts)
# ═══════════════════════════════════════════════════════════════════════════
# a) Crie a coluna `economia_reais` = regular_price - promotional_price
#
# b) Crie a coluna `status_promo` usando .map():
#    True  → "Em promoção"
#    False → "Preço cheio"
#
# c) Filtre apenas produtos de "Perfumaria" e calcule a MÉDIA de economia_reais.
#    Imprima o valor com 2 casas decimais.

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 4 — Faixas de preço com pd.cut() (1 pt)
# ═══════════════════════════════════════════════════════════════════════════
# Crie a coluna `faixa_preco` dividindo promotional_price em:
#   Até R$ 50      → de 0 a 50
#   R$ 50-100      → de 50 a 100
#   R$ 100-200     → de 100 a 200
#   Acima de R$ 200 → acima de 200
#
# Conte quantos produtos estão na faixa "Até R$ 50" e imprima o resultado.

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 5 — Ordenação (1 pt)
# ═══════════════════════════════════════════════════════════════════════════
# Encontre os 3 produtos da categoria "Cabelos" com MAIOR discount_percentage.
# Imprima apenas as colunas "name" e "discount_percentage".

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 6 — Agrupamento (1,5 pts)
# ═══════════════════════════════════════════════════════════════════════════
# Use groupby em "normalized_category" para calcular:
#   - preço promocional médio  (coluna: preco_medio)
#   - quantidade de produtos   (coluna: qtd_produtos)
#
# Ordene pelo preco_medio (do maior para o menor) e mostre o resultado completo.
# Qual categoria tem o preço promocional médio mais alto? Imprima o nome dela.

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 7 — Limpeza de dados (1 pt)
# ═══════════════════════════════════════════════════════════════════════════
# O dataset tem produtos repetidos (mesmo `code` em linhas diferentes).
# a) Imprima quantas linhas existem ANTES de remover duplicatas.
# b) Remova duplicatas mantendo apenas a primeira ocorrência de cada `code`.
# c) Imprima quantas linhas restaram DEPOIS.

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# TAREFA 8 — Filtro combinado (1,5 pts)
# ═══════════════════════════════════════════════════════════════════════════
# Filtre produtos que:
#   - têm "Vegano" na coluna features (dica: use .str.contains("Vegano", na=False))
#   - estão em promoção (promotion_active == True)
#   - têm desconto maior que 40% (discount_percentage > 40)
#
# Imprima:
#   a) Quantos produtos atendem aos 3 critérios
#   b) O nome e o desconto do produto com maior discount_percentage nesse grupo

# TODO: seu código aqui


# ═══════════════════════════════════════════════════════════════════════════
# DESAFIO FINAL — BÔNUS (2 pts)
# ═══════════════════════════════════════════════════════════════════════════
# Monte um "relatório da linha Malbec" com as seguintes informações:
#
#   1. Total de produtos da linha "Malbec"
#   2. Quantos estão em promoção
#   3. Preço promocional médio da linha
#   4. Produto com maior desconto (nome + percentual)
#   5. Categoria (normalized_category) mais frequente entre os produtos Malbec
#
# Dica: você pode usar filtros, groupby, value_counts e sort_values juntos.
# Formate a saída de forma legível, como um mini-relatório em texto.

# TODO: seu código aqui
