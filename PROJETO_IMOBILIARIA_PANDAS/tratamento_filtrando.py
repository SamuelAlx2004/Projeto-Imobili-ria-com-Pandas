from main import df

# Substituir valores nulos
df = df.fillna(0)

# Removendo registros
registros_remover = df.query('Valor == 0 | Condominio == 0').index
df.drop(registros_remover, axis=0, inplace=True)

# Filtrar apenas apartamentos e remover a coluna 'Tipo'
df = df.query('Tipo == "Apartamento"')
df.drop('Tipo', axis=1, inplace=True)

print(df)

#Aplicando filtros

selecao1 = df['Quartos'] == 1

selecao2 = df['Valor'] < 1200

selecao_final = (selecao1) & (selecao2)

df_filtrado1 = df[selecao_final]

#filtros 2

selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)

 