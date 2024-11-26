import pandas as pd
import matplotlib.pyplot as plt

# URL do conjunto de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Leitura dos dados
dados = pd.read_csv(url, sep=';')

#Criando colunas numéricas
dados.fillna(0,inplace = True)
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']


#Criando uma coluna categorica

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'

#Criando uma coluna binária

dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")

