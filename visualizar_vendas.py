
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 1. Ler os dados
df = pd.read_csv("vendas.csv", parse_dates=["data"])

# 2. Calcular o faturamento de cada venda
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

# 3. Preparar os dados para os gráficos
df["mes"] = df["data"].dt.to_period("M").astype(str)

faturamento_mensal = (
    df.groupby("mes")["faturamento"]
    .sum()
    .reset_index()
)

vendas_por_produto = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

faturamento_por_categoria = (
    df.groupby("categoria")["faturamento"]
    .sum()
    .reset_index()
)

# 4. Configuração visual
sns.set_theme(style="whitegrid")

# 5. Matplotlib: faturamento mensal
plt.figure(figsize=(10, 5))
plt.plot(
    faturamento_mensal["mes"],
    faturamento_mensal["faturamento"],
    marker="o"
)
plt.title("Faturamento mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("faturamento_mensal.png", dpi=150)
plt.close()

# 6. Seaborn: quantidade vendida por produto
plt.figure(figsize=(10, 5))
sns.barplot(
    data=vendas_por_produto,
    x="quantidade",
    y="produto"
)
plt.title("Quantidade vendida por produto")
plt.xlabel("Unidades vendidas")
plt.ylabel("Produto")
plt.tight_layout()
plt.savefig("vendas_por_produto.png", dpi=150)
plt.close()

# 7. Seaborn: faturamento por categoria
plt.figure(figsize=(8, 5))
sns.barplot(
    data=faturamento_por_categoria,
    x="categoria",
    y="faturamento"
)
plt.title("Faturamento por categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.savefig("faturamento_por_categoria.png", dpi=150)
plt.close()

# 8. Plotly: gráfico interativo mensal
fig = px.bar(
    faturamento_mensal,
    x="mes",
    y="faturamento",
    title="Faturamento mensal interativo",
    labels={
        "mes": "Mês",
        "faturamento": "Faturamento (R$)"
    },
    text_auto=".2f"
)

fig.write_html("faturamento_interativo.html")

# 9. Resumo dos resultados
print("\nRESUMO DAS VENDAS")
print("Quantidade de registros:", len(df))
print("Unidades vendidas:", df["quantidade"].sum())
print(f"Faturamento total: R$ {df['faturamento'].sum():,.2f}")

print("\nFATURAMENTO MENSAL")
print(faturamento_mensal.to_string(index=False))

print("\nGRÁFICOS CRIADOS")
print("- faturamento_mensal.png")
print("- vendas_por_produto.png")
print("- faturamento_por_categoria.png")
print("- faturamento_interativo.html")
