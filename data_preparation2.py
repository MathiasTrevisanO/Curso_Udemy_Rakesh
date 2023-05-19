
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Dropna 

## Le o dataset com valores vazios
# employee = pd.read_csv('C:\\Users\\mathi\OneDrive\\Área de Trabalho\\Cursos\\Curso_Udemy_Rakesh\\Tab_separated_values_missing_values.tsv', 
                    #    sep='\t')

# Exibe os dados carregados
# print(employee.head())
# print(employee.shape)

#Dropna para todos os NaNs
# print(employee.dropna(how='any').shape)

##Dropna somente no nome e no salario
# print(employee.dropna(subset=['Name','Salary'], how='any').shape)

##fillna para preencher os NaNs com zero
# df_fill_zero = employee.Salary.fillna(0)
# print(df_fill_zero)
##preenche os Nans com a média

##retira o $ do salario
# print(employee.Salary.replace({'\$': ''}, regex = True))

## Dataset da produção de leite por mês
# data = pd.read_csv('C:\\Users\\mathi\OneDrive\\Área de Trabalho\\Cursos\\Curso_Udemy_Rakesh\\monthly-milk-production-pounds.csv')

# plt.plot(data.index.values, data.loc[0:,'Monthly milk production (pounds per cow)'])
# plt.xlabel('Dias')
# plt.ylabel('Pounds por vaca')
# plt.title('Monthly milk production.')
# plt.show()

##conceito de joins
df1 = pd.DataFrame({
    "employee": ["ABC", "XYZ", "MNO"],
    "Age": ["22", "25", "30"]
})
print(df1)

df2 = pd.DataFrame({
    "employee": ["ABC", "XYZ", "PQR"],
    "salary": ["10000", "125000", "30000"]
})
print(df2)

##outer join
df3 = pd.merge(df1,df2, on="employee", how="outer")
print(df3)

##left
df3 = pd.merge(df1,df2, on="employee", how="left")
print(df3)

##right
df3 = pd.merge(df1,df2, on="employee", how="right")
print(df3)
