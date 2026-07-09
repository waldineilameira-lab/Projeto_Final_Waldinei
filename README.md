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

## Query 2 — Funcionários por Região (com localização)

**Objetivo:** analisar a distribuição geográfica dos salários, relacionando funcionários a cidade, estado, país e região.

**Tabelas utilizadas:** EMPLOYEES (funcionários), DEPARTMENTS (departamentos), LOCATIONS (localizações), COUNTRIES (países) e REGIONS (regiões).

**Relacionamento:** EMPLOYEES com LEFT JOIN em DEPARTMENTS (via DEPARTMENT_ID), LOCATIONS (via LOCATION_ID), COUNTRIES (via COUNTRY_ID) e REGIONS (via REGION_ID) — uma cadeia de 4 LEFT JOINs que percorre do funcionário até a região onde seu departamento está localizado.

**Filtro aplicado:** `WHERE REGION_NAME IS NOT NULL`, garantindo que só entrem registros com uma região geográfica de fato associada, descartando quebras na cadeia de relacionamento.

**Arquivo da consulta:** `sql/query_02_funcionarios_regiao.sql`
**Arquivo de dados exportado:** `data/query_02.csv`

**Observação inicial:** já é possível notar diferenças salariais expressivas mesmo dentro da mesma região. Por exemplo, funcionários em Toronto (Canadá) e Seattle (EUA), ambos na região "Americas", apresentam faixas salariais bem distintas — um ponto que será aprofundado na Análise Exploratória de Dados.
