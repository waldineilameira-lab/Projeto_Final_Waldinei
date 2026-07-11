"""
Projeto Final - Análise de Dados de RH
Aluno: Waldinei Lameira Rosa
Turma: Visualização de Dados e Business Intelligence

Este script realiza a Análise Exploratória de Dados (AED) sobre as
bases extraídas via SQL (Query 1 e Query 2) do esquema HR do FreeSQL.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("Bibliotecas instaladas com sucesso!!!")

# ============================================================
# QUERY 1 - Salário por Departamento e Cargo
# ============================================================

# Carregando o arquivo da base query 1
df = pd.read_csv("data/query_01.csv")

# Renomeando as colunas para português
df = df.rename(columns={
    'EMPLOYEE_ID': 'id_empregado',
    'FIRST_NAME': 'nome',
    'LAST_NAME': 'sobrenome',
    'JOB_TITLE': 'cargo',
    'DEPARTMENT_NAME': 'departamento',
    'SALARY': 'salario'
})

print("\n--- Query 1: primeiras linhas ---")
print(df.head())

# Verificando a estrutura da base
print("\n--- Query 1: shape ---")
print(df.shape)

# Verificando valores ausentes
print("\n--- Query 1: valores ausentes ---")
print(df.isnull().sum())

# Verificando valores duplicados
print("\n--- Query 1: valores duplicados ---")
print(df.duplicated().sum())

# Estatísticas descritivas
print("\n--- Query 1: estatísticas descritivas do salário ---")
print(df[["salario"]].describe().round(2))

# ============================================================
# QUERY 2 - Funcionários por Região
# ============================================================

# Carregando o arquivo da base query 2
df2 = pd.read_csv("data/query_02.csv")

# Renomeando as colunas para português
df2 = df2.rename(columns={
    'EMPLOYEE_ID': 'id_empregado',
    'FIRST_NAME': 'nome',
    'LAST_NAME': 'sobrenome',
    'DEPARTMENT_NAME': 'departamento',
    'CITY': 'cidade',
    'STATE_PROVINCE': 'estado',
    'COUNTRY_NAME': 'pais',
    'REGION_NAME': 'regiao',
    'SALARY': 'salario'
})

print("\n--- Query 2: primeiras linhas ---")
print(df2.head())

# Verificando a estrutura da base
print("\n--- Query 2: shape ---")
print(df2.shape)

# Verificando valores ausentes
print("\n--- Query 2: valores ausentes ---")
print(df2.isnull().sum())

# Verificando valores duplicados
print("\n--- Query 2: valores duplicados ---")
print(df2.duplicated().sum())

# Estatísticas descritivas
print("\n--- Query 2: estatísticas descritivas do salário ---")
print(df2[["salario"]].describe().round(2))

# ============================================================
# VISUALIZAÇÕES
# ============================================================

# Histograma - distribuição geral de salários (Query 1)
plt.figure(figsize=(10, 6))
sns.histplot(df['salario'], bins=15, kde=True, color='steelblue')
plt.title('Distribuição de Salários - Query 1 (Departamento e Cargo)')
plt.xlabel('Salário (R$)')
plt.ylabel('Frequência')
plt.show()

# Boxplot - salário por departamento (Query 1)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='departamento', y='salario', hue='departamento', palette='Set2', legend=False)
plt.title('Salário por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot - salário por região (Query 2)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df2, x='regiao', y='salario', hue='regiao', palette='Set3', legend=False)
plt.title('Salário por Região')
plt.xlabel('Região')
plt.ylabel('Salário (R$)')
plt.tight_layout()
plt.show()

# Salário médio por departamento, ordenado do maior para o menor
media_por_departamento = df.groupby('departamento')['salario'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
media_por_departamento.plot(kind='bar', color='teal')
plt.title('Salário Médio por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário Médio (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Contagem de funcionários por faixa salarial
faixas = pd.cut(df['salario'], bins=[0, 8000, 12000, 16000, 25000],
                 labels=['Até 8k', '8k-12k', '12k-16k', 'Acima de 16k'])
contagem_faixas = faixas.value_counts().sort_index()

plt.figure(figsize=(8, 5))
contagem_faixas.plot(kind='bar', color='coral')
plt.title('Distribuição de Funcionários por Faixa Salarial')
plt.xlabel('Faixa Salarial')
plt.ylabel('Quantidade de Funcionários')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================================
# IDENTIFICAÇÃO DE OUTLIERS (método IQR)
# ============================================================

# Outliers de salário - Query 1
Q1 = df['salario'].quantile(0.25)
Q3 = df['salario'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['salario'] < limite_inferior) | (df['salario'] > limite_superior)]
print("\n--- Query 1: Outliers de salário ---")
print("Limite inferior: {limite_inferior}")
print("Limite superior: {limite_superior}")
print("Quantidade de outliers: {len(outliers)}")
print(outliers)

# Outliers de salário - Query 2
Q1_2 = df2['salario'].quantile(0.25)
Q3_2 = df2['salario'].quantile(0.75)
IQR_2 = Q3_2 - Q1_2
limite_inferior_2 = Q1_2 - 1.5 * IQR_2
limite_superior_2 = Q3_2 + 1.5 * IQR_2

outliers_2 = df2[(df2['salario'] < limite_inferior_2) | (df2['salario'] > limite_superior_2)]
print("\n--- Query 2: Outliers de salário ---")
print("Limite inferior: {limite_inferior_2}")
print("Limite superior: {limite_superior_2}")
print("Quantidade de outliers: {len(outliers_2)}")
print(outliers_2)

print("\nAnálise concluída!")
