'''
OBS: Para análise de dados é ideal usar a extensão .ipynb, ela proprociona melhor vizualização da tabelas da Base de Dados, além de ser a extensão mais adequada para trabalhar com análise. Caso queira teste isso, copie todo o código e troque todos os "print" para "display", isso vai alterar a forma que as tabelas são apresentadas na saída do código
'''

# Passo a Passo do Projeto
    # # Passo 1: Importar a Base de Dados;
    # # Passo 2: Vizualizar a Base de Dados;
    # # Passo 3: Indentificar os problemas e corrigi-los;
    # # Passo 4: Análise inicial dos cancelamentos;
    # # Passo 5: Análise das causas dos cancelamentos;
        # # Como as colunas da base impactam no cancelamento?

# Executando Passo 1:
import pandas as pd
baseDeDados = pd.read_csv('cancelamentos.csv')

# Execuntando Passo 2:
print(baseDeDados)

# Executando Passo 3:
    # Problemas:
        # Colunas inúteis -> "Informações que não te ajudam, te atrapalham!"
            # CustomerID
        # Valores vazios

'Colunas inúteis'
baseDeDados = baseDeDados.drop(columns='CustomerID')
print(baseDeDados)

'Valores Vazios'

print(baseDeDados.info())

# Excluir valores vazios

baseDeDados = baseDeDados.dropna()
print(baseDeDados.info())

# Executando passo 4:
    # Quantas pessoas cancelaram e quantas pessoas não cancelaram?
    # Depois em percentual
    
'Pessoas que cancelaram'

print(baseDeDados['cancelou'].value_counts())

'Em percentual'

print(baseDeDados["cancelou"].value_counts(normalize=True))

# O Normalize é um procedimento estatistico que coloca os valores na base de 0 à 1, nosso caso 56% dos clientes cancelaram e 43% não cancelaram

# Executando passo 5:
    # Criar gráficos/dashboards, para isso vamos usar a bib plotly

import plotly.express as px

for coluna in baseDeDados.columns:
    # Criar gráfico
    grafico = px.histogram(baseDeDados, x=coluna, color='cancelou')

    # Exibir gráfico
    grafico.show()

# Análise Qualitativas
    # Conclusões retiradas a partir da análise dos gráficos
        # Clientes do contraro mensal, TODOS, cancelam
            # Oferecer descontos nos planos anuais e trimestrais
            
        # Clientes que ligam mais de 4 vezes para o call center, cancelam com maior frequência
            # Criar um processo para resolver o problema do cliente em no máximo 3 ligações
        
        # Clientes que atrasaram mais de 20 dias, cancelaram
            # Politica de resolver atrasos até 10 dias (Equipe Financeira)
          
'Retirando os problemas, resultado cumulativo'

baseDeDados = baseDeDados[baseDeDados['duracao_contrato'] != 'Monthly']
baseDeDados = baseDeDados[baseDeDados['ligacoes_callcenter'] <= 4]
baseDeDados = baseDeDados[baseDeDados['dias_atraso'] <= 20]

'Pessoas que cancelaram, novo percentual'

print(baseDeDados['cancelou'].value_counts())

'Em percentual'

print(baseDeDados["cancelou"].value_counts(normalize=True))

'''
Análise Final

Antes de reconhecer todos os maiores problemas da empresa, tinhamos um valor de 56% de cancelamentos, após a identificação desses problemas e aplicadas algumas soluções, o valor estimado de cancelamento é de 18%, ou seja, conseguimos diminir a taxa de cancelamento em 38%.
'''
