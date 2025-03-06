import pandas as pd

df = pd.read_csv('C:/Users/gabri/Dropbox/PC (2)/Documents/estudos/infinity/projeto_final/sales_data_sample.csv', sep=',', encoding='latin1')

df = df[df['STATUS'].isin(['Shipped', 'Resolved'])]# Removendo linhas com pedidos mal sucedidos
df = df.drop(columns=['ADDRESSLINE2', 'STATE', 'POSTALCODE', 'TERRITORY', 'CONTACTFIRSTNAME', 'CONTACTLASTNAME', 'ORDERNUMBER','YEAR_ID', 'MONTH_ID', 'PHONE', 'MSRP', 'DEALSIZE', 'PRODUCTCODE', 'CITY', 'ADDRESSLINE1'])# Removendo colunas que não vão agregar à análise

df['ORDERDATE'] = df['ORDERDATE'].str.split(' ').str[0]# Removendo a hora da data
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], format='%m/%d/%Y')# Convertendo a data para o formato datetime
df = df.sort_values(by=['ORDERDATE','ORDERLINENUMBER'])# Ordenando o dataframe pela data e ordem a qual o pedido foi feito
df['ORDERDATE'] = df['ORDERDATE'].dt.strftime('%d/%m/%Y') # Convertendo a data para o formato brasileiro

df['SALES'] = (df['QUANTITYORDERED'] * df['PRICEEACH']).round(2) # Alterando a coluna SALES para o valor do faturamento


df.to_csv('C:/Users/gabri/Dropbox/PC (2)/Documents/estudos/infinity/projeto_final/treated_sales_data_sample.csv', sep=',', encoding='latin1', index=False)

df_2003 = df[df['ORDERDATE'].str.contains('2003')]# Separando os dados de 2003 para estudo
df_general = df[df['ORDERDATE'].str.contains('2004', '2005')]# Separando os dados gerais para estudo

df_2003.to_csv('C:/Users/gabri/Dropbox/PC (2)/Documents/estudos/infinity/projeto_final/2003_sales_data_sample.csv', sep=',', encoding='latin1', index=False)
df_general.to_csv('C:/Users/gabri/Dropbox/PC (2)/Documents/estudos/infinity/projeto_final/general_sales_data_sample.csv', sep=',', encoding='latin1', index=False)

