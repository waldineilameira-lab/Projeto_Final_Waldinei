# Projeto_Final_Waldinei
Repositório do projeto final no módulo I de Visualisação de Dados e Bisiness Intelligence

## Query 1 — Salário por Departamento e Cargo

**Objetivo:** analisar a distribuição de salários cruzando informações de cargo e departamento.

**Tabelas utilizadas:** EMPLOYEES (funcionários), DEPARTMENTS (departamentos) e JOBS (cargos).

**Relacionamento:** EMPLOYEES com LEFT JOIN em DEPARTMENTS (via DEPARTMENT_ID) e LEFT JOIN em JOBS (via JOB_ID). O LEFT JOIN garante que nenhum funcionário seja excluído do resultado mesmo que não tenha departamento ou cargo vinculado.

**Filtro aplicado:** `WHERE SALARY > 5000`, focando na faixa de salários médios e altos da empresa.

**Arquivo da consulta:** `sql/query_01_salario_departamento_cargo.sql`
**Arquivo de dados exportado:** `data/query_01.csv`

**Observação inicial:** já é possível notar uma diferença expressiva entre cargos operacionais (ex: Public Accountant, R$8.300) e cargos executivos (ex: President, R$24.000), o que será aprofundado na Análise Exploratória de Dados.
