import pandas as pd
import matplotlib.pyplot as plt

# URL do conjunto de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Leitura dos dados
dados = pd.read_csv(url, sep=';')

# Definição dos tipos de imóveis comerciais
imoveis_comerciais = [
    'Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão',
    'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão',
    'Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara',
    'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 'Hotel', 'Indústria'
]

# Filtrando imóveis que NÃO são comerciais
df = dados.query('@imoveis_comerciais not in Tipo')

# ===============================
# 1. Valor médio de aluguel por tipo de imóvel
# ===============================

# Agrupando por tipo e calculando a média do valor do aluguel
tipo_media_valor = (
    df.groupby('Tipo')[['Valor']]
    .mean()
    .sort_values('Valor')
)

# Plotando o gráfico de barras horizontais
ax = tipo_media_valor.plot(
    kind='barh', figsize=(14, 10), color='purple'
)
ax.set_title('Valor Médio de Aluguel por Tipo de Imóvel', fontsize=16)
ax.set_xlabel('Valor Médio (R$)', fontsize=14)
ax.set_ylabel('Tipos de Imóveis', fontsize=14)
plt.show()

# ===============================
# 2. Percentual de cada tipo de imóvel
# ===============================

# Calculando o percentual de cada tipo de imóvel
df_percentual_tipo = (
    df['Tipo']
    .value_counts(normalize=True)
    .to_frame()
    .sort_values('Tipo')
)

# Renomeando a coluna para facilitar a interpretação
df_percentual_tipo.columns = ['Percentual']

# Plotando o gráfico de barras
ax = df_percentual_tipo.plot(
    kind='bar', figsize=(14, 10), color='green', edgecolor='black'
)
ax.set_title('Distribuição Percentual por Tipo de Imóvel', fontsize=16)
ax.set_xlabel('Tipos de Imóveis', fontsize=14)
ax.set_ylabel('Percentual', fontsize=14)
plt.show()
