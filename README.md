# Análise e Visualização de Vendas com Python

## Sobre o projeto

Este projeto realiza uma análise exploratória de dados de vendas utilizando Python. O objetivo é transformar uma base de dados em gráficos que facilitem a compreensão do desempenho comercial.

A solução calcula o faturamento das vendas, agrupa os resultados por mês, produto e categoria e gera visualizações estáticas e interativas.

## Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Pandas** — leitura, transformação e análise dos dados.
- **Matplotlib** — criação de gráficos estáticos.
- **Seaborn** — visualização e comparação de dados.
- **Plotly Express** — criação de gráficos interativos.

## Funcionalidades

- Leitura dos dados de vendas a partir de um arquivo CSV.
- Cálculo do faturamento de cada registro.
- Agrupamento do faturamento por mês.
- Análise da quantidade vendida por produto.
- Comparação do faturamento por categoria.
- Exportação dos gráficos para arquivos PNG e HTML.
- Exibição de indicadores resumidos no terminal.

## Estrutura do projeto

```text
visualizacao_vendas/
├── vendas.csv
├── visualizar_vendas.py
├── faturamento_mensal.png
├── vendas_por_produto.png
├── faturamento_por_categoria.png
├── faturamento_interativo.html
├── README.md
└── .gitignore
```

Os quatro arquivos de gráficos são gerados após a execução do programa.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/visualizacao_vendas.git
cd visualizacao_vendas
```

Substitua `SEU-USUARIO` pelo seu nome de usuário do GitHub.

### 2. Criar um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as bibliotecas

```bash
python -m pip install pandas matplotlib seaborn plotly
```

### 4. Executar o programa

```bash
python visualizar_vendas.py
```

### 5. Visualizar os resultados

Os gráficos PNG podem ser abertos em um visualizador de imagens. Para explorar o gráfico interativo, abra `faturamento_interativo.html` em um navegador.

## Indicadores analisados

- Quantidade de registros processados.
- Total de unidades vendidas.
- Faturamento total.
- Evolução mensal do faturamento.
- Quantidade vendida por produto.
- Faturamento por categoria.

## Aprendizados

Este projeto permite praticar manipulação de dados com Pandas, agrupamentos, cálculos de indicadores, construção de gráficos e comunicação visual de informações de negócios.

## Possíveis melhorias

- Criar um dashboard interativo completo.
- Adicionar filtros por período, produto e cidade.
- Calcular ticket médio e crescimento mensal.
- Implementar validações para dados ausentes ou inconsistentes.
- Adicionar testes automatizados.

## Observação

Os resultados dependem dos dados presentes em `vendas.csv`. Os valores exibidos no terminal e nos gráficos são calculados a partir desse arquivo.

## Autor

Projeto desenvolvido para fins de estudo e portfólio em análise e visualização de dados.
