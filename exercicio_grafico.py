import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('C:/Users/Cliente/Downloads/ecommerce_preparados.csv')

print(df.head().to_string())
print(df.dtypes)



# Converte colunas que deveriam ser numéricas
df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')
df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')

# Trata coluna de avaliações (ex: '+10mil')
df['N_Avaliações'] = (
    df['N_Avaliações']
    .astype(str)
    .str.replace('+', '', regex=False)
    .str.replace('mil', '000')
)

df['N_Avaliações'] = pd.to_numeric(df['N_Avaliações'], errors='coerce')


plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=50, color='green', alpha=0.8)
plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 6))
plt.hexbin(df['Preço'], df['Nota'], gridsize=40, cmap='Blues')
plt.colorbar(label='Quantidade de produtos')
plt.xlabel('Preço')
plt.ylabel('Nota')
plt.title('Densidade de Preço vs Nota')
plt.show()


colunas_corr = ['Preço', 'Nota', 'N_Avaliações', 'Qtd_Vendidos']
corr = df[colunas_corr].corr()

plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação')
plt.show()


vendas_por_marca = (
    df.groupby('Marca')['Qtd_Vendidos']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
vendas_por_marca.plot(kind='bar', color='#90ee90')
plt.title('Top 10 Marcas por Quantidade Vendida')
plt.xlabel('Marca')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.show()


vendas_top5 = vendas_por_marca.head(5)

plt.figure(figsize=(8, 8))
plt.pie(
    vendas_top5.values,
    labels=vendas_top5.index,
    autopct='%.1f%%',
    startangle=90
)
plt.title('Distribuição de Vendas - Top 5 Marcas')
plt.show()


plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Preço'], color='lightblue')
plt.title('Boxplot do Preço')
plt.xlabel('Preço')
plt.show()


plt.figure(figsize=(8, 6))
sns.regplot(
    x='Preço',
    y='Qtd_Vendidos',
    data=df,
    scatter_kws={'alpha': 0.4},
    line_kws={'color': 'red'}
)
plt.title('Regressão: Preço vs Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()
