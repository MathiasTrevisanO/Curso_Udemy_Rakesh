import pandas as pd
import numpy as np
# Carrega o arquivo TSV
employee = pd.read_csv('C:\\Users\\mathi\OneDrive\\Área de Trabalho\\Cursos\\Curso_Udemy_Rakesh\\Tab_separated_values.tsv', sep='\t')

# Exibe os dados carregados
print(employee.head())

# olhe certas colunas no Dataset
cols = ['Name', 'Position']
# print(employee[cols].head())

# # display integer datatypes
# print(employee.dtypes)
# print(employee.select_dtypes(include= [np.number]).dtypes)

# # metodos para analise de dados

# print(employee.describe())
# print(employee.shape) # linha e coluna
# print(type(employee))

##concatenar 2 colunas
# employee['Name Salary'] = employee['Name'] + employee['Salary']
# print(employee.head())

##remover coluna
# employee.drop('Office', axis= 1, inplace = True)
# print(employee.head())

##modificar o nome das colunas
# cols = ['Name', 'Position', 'Ofc', 'Age', 'StartDate', 'Sal']
# employee.columns = cols
# print(employee.head())

## ordem crescente ou decrescente na tabela pela idade
# print(employee.sort_values(by= 'Age', ascending=True).head())
# #ordem crescente dos nomes
# print(employee['Name'].sort_values().head())

##Filtra onde idade menor que 40
# print(employee[employee.Age < 40].head())

##Outra condição de filtragem
# print(employee[(employee.Age < 40) & (employee.Name == "Airi Satou")])

# cols = ['Name', 'Position']
# print(employee[employee.Age < 40][cols].head())

## Exercicio de Filtrar nomes
# print(employee[(employee.Name == "Airi Satou") | (employee.Name == "Brenden Wagner") | (employee.Name == "Bruno Nash")])

##Calculo da média das idades
# print(employee.Age.mean())

##deixar o nome tudo maiusculo ou minusculo
# print(employee.Name.str.upper().head())
# print(employee.Name.str.lower().head())


# print(employee.Position.str.contains('Software')) ##retorna T or F position que contém software
# print(employee[employee.Position.str.contains('Software')]) #retorna quem tem a position software

##substitui a palavra engineer por developer
# print(employee.Position.str.replace('Engineer', 'Developer').head())

##-----------------------------aggregations----------------------------------

##idade minima e maxima
# print(employee.Age.min())
# print(employee.Age.max())

##groupby - agrupa a posição com a idade
# print(employee.groupby('Position').Age.min().head())
# print(employee.groupby('Position').Age.agg(['count', 'min', 'max']).head())

##exercicio de agrupar o salario e a idade e fazer a media
# print(employee.groupby('Salary').Age.mean())

##----------------------------------------------------------------------------

## escolher as linhas e colunas pelo loc
# print(employee.loc[0,:])
# print(employee.loc[0:2, :])
# print(employee.loc[0:2, ['Name', 'Position']])
# print(employee.loc[0:2, 'Name':'Office'])

##linhas com uma certa condição
# print(employee.loc[employee.Position == 'Accountant', :])


