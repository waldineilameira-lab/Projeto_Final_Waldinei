# Projeto Final — Análise de Dados de RH

**Aluno:** Waldinei Lameira Rosa
**Turma:** Visualização de Dados e Business Intelligence

## Sobre este projeto

Este repositório é o projeto final do módulo de Visualização de Dados e Business Intelligence. A proposta foi vestir o papel de analista de dados dentro de uma área de Recursos Humanos: uma empresa fictícia precisava entender melhor como seus salários estão distribuídos entre cargos, departamentos e regiões geográficas, e coube a mim buscar essas respostas usando SQL, Python e um pouco de estatística.

Mais do que cumprir os requisitos técnicos, entendi este projeto como uma oportunidade de simular uma rotina real de análise: ir até o banco de dados, extrair o que interessa, tratar o que vem torto, e transformar números soltos numa história que faça sentido para quem vai tomar decisão — no caso, o time de RH.

## Objetivo do trabalho

A partir da base HR (Human Resources) do FreeSQL, o desafio era responder três perguntas centrais:

- Como os salários estão distribuídos entre cargos e departamentos?
- Existe um padrão de remuneração relacionado à localização geográfica dos funcionários?
- O que esses dados revelam sobre a estrutura salarial da empresa, e o que isso significa na prática para novas contratações?

Para isso, desenvolvi duas consultas SQL, exportei os resultados para CSV, e conduzi uma Análise Exploratória de Dados (AED) em Python.

## Tabelas utilizadas

A base HR reúne informações de funcionários, cargos, departamentos e localização, organizadas em seis tabelas principais:

- **EMPLOYEES** — dados de cada funcionário: nome, cargo, departamento e salário.
- **JOBS** — o catálogo de cargos existentes na empresa.
- **DEPARTMENTS** — os departamentos e a que localização cada um pertence.
- **LOCATIONS** — cidade e estado de cada unidade da empresa.
- **COUNTRIES** — os países onde a empresa atua.
- **REGIONS** — o agrupamento geográfico mais amplo (ex: Americas, Europe).

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

## A análise em Python

Toda a análise foi feita com pandas, matplotlib e seaborn, e está documentada em [`analise_rh.py`](analise_rh.py). O caminho que segui foi:

1. Carreguei os dois CSVs e renomeei as colunas para português, deixando a leitura mais natural.
2. Chequei se havia valores ausentes ou duplicados — pequeno cuidado que sempre vale a pena antes de confiar em qualquer número.
3. Calculei as estatísticas básicas (média, mediana, mínimo e máximo) para entender a "temperatura" geral dos salários.
4. Visualizei a distribuição com um histograma, e depois usei boxplots para comparar salários entre departamentos e entre regiões.
5. Identifiquei outliers usando o método do intervalo interquartil (IQR), para saber quais salários realmente fogem do padrão — e por quê.
6. Fechei com dois gráficos de barras: um comparando a média salarial por departamento, e outro mostrando quantos funcionários estão em cada faixa de salário.

### O que os dados mostraram

Ao carregar os dois arquivos, encontrei uma pequena lacuna: 1 registro sem departamento preenchido na Query 1, e 1 sem estado preenchido na Query 2. São casos isolados que não atrapalham a análise, mas mostram que, mesmo numa base pequena, vale sempre checar antes de assumir que os dados estão completos.


|
 Métrica
|
 Query 1 (salário > R$5.000)
|
 Query 2 (todos, com região)
|
|
---
|
---
|
---
|
|
 Registros
|
 58
|
 106
|
|
 Média
|
 R$ 9.298,55
|
 R$ 6.456,75
|
|
 Mediana
|
 R$ 8.500,00
|
 R$ 6.150,00
|
|
 Mínimo
|
 R$ 5.800,00
|
 R$ 2.100,00
|
|
 Máximo
|
 R$ 24.000,00
|
 R$ 24.000,00
|

A diferença de média entre as duas bases faz sentido: a Query 1 já parte de um piso salarial de R$5.000, enquanto a Query 2 traz o quadro completo, incluindo cargos de entrada.

## Principais insights

**1. Os salários não seguem uma distribuição "equilibrada".** O histograma deixa isso bem visível: a maior parte dos funcionários está concentrada entre R$5.800 e R$10.000, e depois há uma cauda longa que se estica até R$24.000. É por isso que a mediana (R$8.500) fica abaixo da média (R$9.298,55) — poucos salários muito altos "puxam" a média para cima.

**2. O departamento Executive está numa liga à parte.** Com salário médio de aproximadamente R$19.300, é quase o dobro do segundo colocado (Purchasing, ~R$11.000). Não por acaso, os três outliers que encontrei via IQR pertencem exatamente a esse departamento: o President e dois Vice Presidents.

**3. A região Americas concentra tanto os extremos mais baixos quanto os mais altos.** O boxplot por região mostrou quatro pontos fora do padrão só dentro da Americas, enquanto a Europe não teve nenhum — mas, curiosamente, a Europe tem uma mediana salarial mais alta (~R$8.800 contra ~R$3.200 da Americas). Ou seja: a Americas é mais desigual internamente, mesmo tendo os salários mais altos da empresa dentro dela.

**4. A empresa é, na maior parte, uma pirâmide bem tradicional.** 86% dos funcionários (50 de 58) recebem até R$12.000. Apenas 5% ultrapassam R$16.000 — e são justamente os mesmos identificados como outliers. Isso reforça que a estrutura salarial tem uma base operacional ampla e um topo executivo pequeno e bem destacado.

## Por que os outliers importam

Poderia ser tentador ignorar os outliers como "ruído" nos dados, mas aqui eles contam uma história real: não são erros de digitação ou falhas na base, são o retrato de uma hierarquia salarial concentrada em poucos cargos de liderança. Entender isso é importante na prática — se uma empresa usar a média geral de salários (R$9.298,55) como referência para definir a proposta de um novo colaborador operacional, ela estaria superestimando o valor, porque essa média está distorcida pelos poucos salários executivos. O caminho mais seguro é olhar a mediana do departamento específico onde a vaga está sendo aberta.

## Recomendação para novas contratações

Com base no que os dados mostraram, minha sugestão seria: para cargos operacionais, usar como referência a mediana salarial do próprio departamento (não a média geral da empresa, que está inflada pelo topo executivo). Para cargos de liderança, a empresa já parece ter uma política salarial bem definida em torno de R$19.000-24.000, que pode servir de parâmetro direto para novas contratações nesse nível.

## Como executar o projeto

1. Clone este repositório.
2. Instale as bibliotecas necessárias:
