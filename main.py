import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df_2003 = pd.read_csv('C:/Users/gabri/Dropbox/PC (2)/Documents/estudos/infinity/projeto_final/2003_sales_data_sample.csv', sep=',', encoding='latin1')
df_2003['ORDERDATE'] = pd.to_datetime(df_2003['ORDERDATE'], format='%d/%m/%Y')

def estatisticas_descritivas(df):
    print(f'Estatísticas Descritivas: \n{df.describe()}')
    print(f'Total De Vendas: \n{df["SALES"].sum()}')
    print(f'Média De Vendas: \n{df["SALES"].mean()}')
    print(f'Mediana De Vendas: \n{df["SALES"].median()}')
    print(f'Desvio Padrão: \n{df["SALES"].std()}')

def visualizacoes_graficas(df):

    df_mensal = df.groupby(pd.Grouper(key='ORDERDATE', freq='M')).sum().reset_index()
    fig = px.line(df_mensal, x='ORDERDATE', y='SALES', title='Tendência de Vendas Mensais em 2003')
    fig.show()
    
    top_countries = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.pie(top_countries, values='SALES', names='COUNTRY', title='Top 10 Países por Volume de Vendas')
    fig.show()
    
    product_types = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False).reset_index()
    fig = px.pie(product_types, values='SALES', names='PRODUCTLINE', title='Vendas por Linha de Produto')
    fig.show()
    
    df['month'] = df['ORDERDATE'].dt.month
    df['day'] = df['ORDERDATE'].dt.day
    heatmap_data = df.groupby(['month', 'day'])['SALES'].sum().unstack().fillna(0)
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data.index,
        colorscale='Rainbow'))
    fig.update_layout(title='Padrões Sazonais de Vendas (Mês x Dia)', xaxis_title='Dia do Mês', yaxis_title='Mês')
    fig.show()
    
    top_customers = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.pie(top_customers, values='SALES', names='CUSTOMERNAME', title='Top 10 Clientes por Volume de Vendas')
    fig.show()
    
    fig = px.box(df, x='QTR_ID', y='SALES', title='Distribuição de Vendas por Trimestre')
    fig.show()
    
    year_sum = df['SALES'].cumsum()
    fig = px.line(x=df['ORDERDATE'], y=year_sum, title='Evolução do Faturamento em 2003')
    fig.show()

def main():
    estatisticas_descritivas(df_2003)
    visualizacoes_graficas(df_2003)

main()