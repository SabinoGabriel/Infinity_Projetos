# Análise de Dados e Previsão de Vendas E-commerce

## Sobre o Projeto

Este projeto realiza uma análise detalhada de dados de vendas de e-commerce e implementa um modelo preditivo para estimar vendas futuras. O projeto combina técnicas de análise exploratória de dados, estatística inferencial e machine learning para extrair insights acionáveis e previsões confiáveis.

## Instalação

### Requisitos

Python 3.8+ é recomendado. Para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

Principais dependências incluem:
- pandas
- numpy
- matplotlib
- plotly
- scikit-learn
- scipy

## Estrutura do Projeto

```
.
├── main.py                        # Script principal de análise e modelagem
├── requirements.txt               # Dependências do projeto
├── 2003_sales_data_sample.csv     # Dados de vendas de 2003 (amostra)
├── general_sales_data_sample.csv  # Dados gerais de vendas (amostra)
├── treated_sales_data_sample.csv  # Dados tratados (gerado pelo script)
├── dataset_inicial_dados.txt      # Metadados do dataset original
├── Projeto Data Science PRO.pptx  # Apresentação do projeto
└── README.md                      # Documentação
```

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SabinoGabriel/Infinity_Projetos.git
   cd Infinity_Projetos
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

4. O script irá processar os dados, gerar visualizações interativas e mostrar resultados da modelagem preditiva.

## Dados

O projeto utiliza dados de vendas de e-commerce contendo os seguintes campos principais:

- **ORDERNUMBER**: Identificador único do pedido
- **QUANTITYORDERED**: Quantidade de itens pedidos
- **PRICEEACH**: Preço unitário
- **SALES**: Valor total da venda
- **ORDERDATE**: Data do pedido
- **STATUS**: Status do pedido (ex: Shipped, Resolved)
- **PRODUCTLINE**: Categoria do produto
- **CUSTOMERNAME**: Nome do cliente
- **COUNTRY**: País do cliente

Os dados abrangem vendas de diferentes categorias de produtos (Classic Cars, Vintage Cars, Motorcycles, etc.) em diversos países ao longo de diferentes períodos.

## Insights Importantes

### Etapas de Pré-processamento
1. **Filtragem de Dados**: 
   - **Objetivo**: Remover registros com status de pedidos mal sucedidos.
   - **Ação**: Mantivemos apenas registros com status 'Shipped' e 'Resolved'.
   - **Resultado**: Foco nas vendas bem-sucedidas.

2. **Remoção de Colunas Desnecessárias**:
   - **Objetivo**: Simplificar o DataFrame.
   - **Ação**: Removemos colunas irrelevantes como ADDRESSLINE2, STATE, POSTALCODE, entre outras.
   - **Resultado**: DataFrame mais enxuto e focado nas variáveis relevantes.

3. **Conversão e Ordenação de Datas**:
   - **Objetivo**: Garantir datas no formato correto e ordenar o DataFrame.
   - **Ação**: Convertemos ORDERDATE para datetime e ordenamos por ORDERDATE e ORDERLINENUMBER.
   - **Resultado**: Datas formatadas corretamente e DataFrame organizado cronologicamente.

### Análise Avançada Implementada

4. **Testes Estatísticos de Hipóteses**:
   - **Objetivo**: Verificar se existe diferença significativa nas vendas entre categorias de produtos.
   - **Ação**: Implementamos teste ANOVA para comparação múltipla entre categorias.
   - **Resultado**: Identificação estatisticamente embasada sobre diferenças entre categorias de produtos.

5. **Preparação de Dados para Machine Learning**:
   - **Objetivo**: Criar features relevantes para modelagem preditiva.
   - **Ação**: Extraímos features temporais (ano, mês, dia, dia da semana) e aplicamos one-hot encoding para variáveis categóricas.
   - **Resultado**: Dataset enriquecido com 20+ features para modelagem.

6. **Validação Cruzada**:
   - **Objetivo**: Garantir robustez do modelo de previsão.
   - **Ação**: Implementamos K-Fold Cross Validation com 5 divisões.
   - **Resultado**: Avaliação mais confiável do modelo, com métricas médias de desempenho e desvio padrão.

7. **Modelagem Preditiva**:
   - **Objetivo**: Prever vendas futuras com base em padrões históricos.
   - **Ação**: Desenvolvemos modelo de regressão linear com avaliação completa (MSE, RMSE, MAE, R²).
   - **Resultado**: Modelo capaz de prever vendas futuras com métricas de desempenho claras.

8. **Previsões para Tomada de Decisão**:
   - **Objetivo**: Fornecer projeções de vendas para o próximo mês.
   - **Ação**: Criamos simulação de vendas futuras baseada em padrões históricos.
   - **Resultado**: Previsões diárias e por categoria de produto para planejamento estratégico.

## Metodologia Aplicada

### Análise Exploratória
- Estatísticas descritivas completas (total, média, mediana, desvio padrão)
- Análises agrupadas por linha de produto, país e temporalidade
- Visualizações diversificadas (tendências, rankings, distribuições, correlações)

### Análise Estatística
- Teste ANOVA para validar hipóteses sobre diferenças entre categorias de produtos
- Interpretação formal dos resultados estatísticos com valor-p

### Fluxo de Machine Learning
1. **Preparação dos dados**: Engenharia de features temporais e codificação de variáveis categóricas
2. **Validação cruzada**: Avaliação robusta com 5-fold cross-validation
3. **Modelagem**: Implementação de regressão linear
4. **Avaliação**: Análise completa de desempenho (MSE, RMSE, MAE, R²)
5. **Previsão**: Geração de estimativas futuras para suporte à decisão

## Resultados e Próximos Passos

### Resultados Alcançados
- Modelo preditivo funcional com métricas de desempenho claras
- Visualizações intuitivas das previsões para facilitar interpretação
- Framework completo de análise, desde a exploração de dados até previsões futuras

### Potenciais Melhorias
- Implementação de modelos mais complexos (Random Forest, XGBoost)
- Detecção e tratamento específico de outliers
- Análise de segmentação de clientes para estratégias personalizadas
- Market basket analysis para identificação de produtos relacionados
- Análise de série temporal para detecção mais precisa de sazonalidade
- Implementação de interface de usuário para interação com o modelo

### Valor para o Negócio
- Suporte à decisão com previsões de vendas baseadas em dados
- Identificação de padrões sazonais e tendências de mercado
- Avaliação quantitativa do desempenho de diferentes categorias de produtos
- Base sólida para otimização de estoque e estratégias de marketing

## Outputs do Projeto

### Visualizações
O script gera diversas visualizações interativas usando Plotly, incluindo:
- Tendências de vendas mensais
- Top países por volume de vendas
- Distribuição de vendas por categoria de produto
- Correlações entre quantidade pedida e valor total
- Padrões sazonais de vendas
- Comparação entre valores reais e previstos
- Previsões para o próximo período

### Métricas de Modelo
O modelo produz métricas de avaliação completas:
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coeficiente de determinação)

### Previsões
As previsões geradas incluem:
- Total de vendas previstas para o próximo mês
- Média de vendas diárias prevista
- Previsões de vendas por dia
- Previsões por categoria de produto
