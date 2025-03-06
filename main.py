import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('treated_sales_data_sample.csv', sep=',', encoding='latin1')

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], format='%d/%m/%Y', errors='coerce')


def estatisticas_descritivas(df):
    print("ESTATÍSTICAS DESCRITIVAS")

    print(f'Estatísticas Descritivas: \n{df.describe()}')
    print(f'Total De Vendas: \n{df["SALES"].sum()}')
    print(f'Média De Vendas: \n{df["SALES"].mean()}')
    print(f'Mediana De Vendas: \n{df["SALES"].median()}')
    print(f'Desvio Padrão: \n{df["SALES"].std()}')
    
    print("\nAnálise Adicional:")
    print(f'Vendas por Linha de Produto:\n{df.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)}')
    print(f'\nVendas por País:\n{df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False).head(10)}')

    df['MONTH'] = df['ORDERDATE'].dt.month
    print(f'\nVendas por Mês:\n{df.groupby("MONTH")["SALES"].sum().sort_index()}')

def visualizacoes_graficas(df):
    print("VISUALIZAÇÕES GRÁFICAS")

    df_mensal = df.groupby(pd.Grouper(key='ORDERDATE', freq='M')).sum().reset_index()
    fig = px.line(df_mensal, x='ORDERDATE', y='SALES', title='Tendência de Vendas Mensais')
    fig.show()
    
    top_countries = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top_countries, x='COUNTRY', y='SALES', title='Top 10 Países por Volume de Vendas', 
                 color='SALES', text_auto=True)
    fig.show()
    
    product_types = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False).reset_index()
    fig = px.pie(product_types, values='SALES', names='PRODUCTLINE', title='Vendas por Linha de Produto',
                hole=0.3)
    fig.show()
    
    fig = px.histogram(df, x='SALES', nbins=50, title='Distribuição das Vendas')
    fig.show()
    
    fig = px.scatter(df, x='QUANTITYORDERED', y='SALES', color='PRODUCTLINE', 
                     title='Correlação entre Quantidade Pedida e Valor Total das Vendas', opacity=0.7)
    fig.show()
    
    df['MONTH'] = df['ORDERDATE'].dt.month
    df['DAY'] = df['ORDERDATE'].dt.day
    
    monthly_sales = df.groupby('MONTH')['SALES'].sum().reset_index()
    fig = px.bar(monthly_sales, x='MONTH', y='SALES', title='Vendas por Mês',
                 labels={'MONTH': 'Mês', 'SALES': 'Total de Vendas'})
    fig.show()
    
    heatmap_data = df.groupby(['MONTH', 'DAY'])['SALES'].sum().unstack().fillna(0)
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data.index,
        colorscale='Viridis'))
    fig.update_layout(title='Padrões Sazonais de Vendas (Mês x Dia)', 
                      xaxis_title='Dia do Mês', 
                      yaxis_title='Mês')
    fig.show()

def teste_hipoteses(df):
    print("TESTES DE HIPÓTESE ESTATÍSTICA")
    
    print("Hipótese: Existe diferença significativa nas vendas entre diferentes categorias de produtos?")
    categories = df['PRODUCTLINE'].unique()
    samples = [df[df['PRODUCTLINE'] == category]['SALES'] for category in categories]
    f_stat, p_value = stats.f_oneway(*samples)
    
    print(f"Estatística F: {f_stat:.4f}")
    print(f"Valor P: {p_value:.4f}")
    if p_value < 0.05:
        print("Conclusão: Rejeitamos a hipótese nula. Há diferença estatisticamente significativa entre as vendas de diferentes categorias de produtos.\n")
    else:
        print("Conclusão: Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que existe diferença significativa entre as vendas de diferentes categorias de produtos.\n")

def preparar_dados_ml(df):
    df['YEAR'] = df['ORDERDATE'].dt.year
    df['MONTH'] = df['ORDERDATE'].dt.month
    df['DAY'] = df['ORDERDATE'].dt.day
    df['DAYOFWEEK'] = df['ORDERDATE'].dt.dayofweek
    
    df_ml = pd.get_dummies(df, columns=['PRODUCTLINE', 'COUNTRY', 'STATUS'], drop_first=True)
    
    features = ['QUANTITYORDERED', 'PRICEEACH', 'MONTH', 'DAY', 'DAYOFWEEK']
    
    cat_features = [col for col in df_ml.columns if col.startswith(('PRODUCTLINE_', 'COUNTRY_', 'STATUS_'))]
    features.extend(cat_features)
    
    X = df_ml[features]
    y = df_ml['SALES']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Número de features utilizadas: {X.shape[1]}")
    print(f"Tamanho do conjunto de treino: {X_train.shape[0]} amostras")
    print(f"Tamanho do conjunto de teste: {X_test.shape[0]} amostras")
    
    return X_train, X_test, y_train, y_test, features

def modelo_machine_learning(X_train, X_test, y_train, y_test, features):
    print("MODELAGEM DE MACHINE LEARNING")
    
    print("\nValidação Cruzada:")
    lr_model_cv = LinearRegression()
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    
    cv_r2_scores = cross_val_score(lr_model_cv, X_train, y_train, cv=kf, scoring='r2')
    cv_neg_mse = cross_val_score(lr_model_cv, X_train, y_train, cv=kf, scoring='neg_mean_squared_error')
    cv_rmse = np.sqrt(-cv_neg_mse)
    
    print(f"CV - R² médio: {cv_r2_scores.mean():.4f} (±{cv_r2_scores.std():.4f})")
    print(f"CV - RMSE médio: {cv_rmse.mean():.4f} (±{cv_rmse.std():.4f})")
    
    cv_results = pd.DataFrame({
        'Fold': range(1, 6),
        'R²': cv_r2_scores,
        'RMSE': cv_rmse
    })
    
    fig = px.line(cv_results, x='Fold', y=['R²', 'RMSE'], markers=True,
                 title='Resultados da Validação Cruzada',
                 labels={'value': 'Valor', 'variable': 'Métrica'})
    fig.show()
    
    # Regressão Linear
    print("\nModelo de Regressão Linear:")
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    
    y_pred_lr = lr_model.predict(X_test)
    
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    rmse_lr = np.sqrt(mse_lr)
    r2_lr = r2_score(y_test, y_pred_lr)
    mae_lr = mean_absolute_error(y_test, y_pred_lr)
    
    print(f"MSE (Erro Quadrático Médio): {mse_lr:.4f}")
    print(f"RMSE (Raiz do Erro Quadrático Médio): {rmse_lr:.4f}")
    print(f"MAE (Erro Absoluto Médio): {mae_lr:.4f}")
    print(f"R² (Coeficiente de determinação): {r2_lr:.4f}")
    
    fig = px.scatter(x=y_test, y=y_pred_lr, labels={'x': 'Vendas Reais', 'y': 'Vendas Previstas'}, title='Regressão Linear: Valores Reais vs Previstos')
    fig.add_shape(type='line', x0=y_test.min(), y0=y_test.min(), x1=y_test.max(), y1=y_test.max(), line=dict(color='red', dash='dash'))
    fig.show()
    
    return lr_model, features

def fazer_previsoes(model, features, df):
    print("PREVISÕES DE VENDAS FUTURAS")
    
    df_future = df.copy()
    
    last_date = df_future['ORDERDATE'].max()
    next_month = last_date + pd.DateOffset(months=1)
    
    df_last_month = df_future[df_future['ORDERDATE'].dt.month == last_date.month]
    avg_orders_per_day = len(df_last_month) / last_date.days_in_month
    days_next_month = next_month.days_in_month
    num_predictions = int(avg_orders_per_day * days_next_month)
    
    print(f"Fazendo {num_predictions} previsões para o próximo mês ({next_month.month}/{next_month.year})")
    
    df_next_month = df_last_month.sample(n=num_predictions, replace=True).copy()
    df_next_month['ORDERDATE'] = [next_month.replace(day=day) for day in range(1, days_next_month + 1) 
                                 for _ in range(int(num_predictions/days_next_month) + 1)][:num_predictions]
    
    df_next_month['YEAR'] = df_next_month['ORDERDATE'].dt.year
    df_next_month['MONTH'] = df_next_month['ORDERDATE'].dt.month
    df_next_month['DAY'] = df_next_month['ORDERDATE'].dt.day
    df_next_month['DAYOFWEEK'] = df_next_month['ORDERDATE'].dt.dayofweek
    
    df_next_month_ml = pd.get_dummies(df_next_month, columns=['PRODUCTLINE', 'COUNTRY', 'STATUS'], drop_first=True)
    
    for feature in features:
        if feature not in df_next_month_ml.columns:
            df_next_month_ml[feature] = 0
    
    X_future = df_next_month_ml[features]
    
    y_future_pred = model.predict(X_future)
    
    df_next_month['PREDICTED_SALES'] = y_future_pred
    
    print(f"\nTotal de vendas previstas para o próximo mês: ${df_next_month['PREDICTED_SALES'].sum():.2f}")
    print(f"Média de vendas diárias prevista: ${df_next_month.groupby('DAY')['PREDICTED_SALES'].mean().mean():.2f}")
    
    daily_pred = df_next_month.groupby('DAY')['PREDICTED_SALES'].sum().reset_index()
    
    fig = px.bar(daily_pred, x='DAY', y='PREDICTED_SALES', title=f'Previsão de Vendas Diárias para {next_month.month}/{next_month.year}',
                 labels={'DAY': 'Dia', 'PREDICTED_SALES': 'Vendas Previstas ($)'})
    fig.show()
    
    if 'PRODUCTLINE' in df_next_month.columns:
        product_pred = df_next_month.groupby('PRODUCTLINE')['PREDICTED_SALES'].sum().sort_values(ascending=False)
        fig = px.bar(product_pred, x=product_pred.index, y=product_pred.values, title=f'Previsão de Vendas por Categoria de Produto para {next_month.month}/{next_month.year}',
                     labels={'index': 'Categoria de Produto', 'y': 'Vendas Previstas ($)'})
        fig.show()
    
    return df_next_month

def main():
    
    estatisticas_descritivas(df)
    visualizacoes_graficas(df)
    
    teste_hipoteses(df)
    
    X_train, X_test, y_train, y_test, features = preparar_dados_ml(df)
    best_model, features = modelo_machine_learning(X_train, X_test, y_train, y_test, features)
    
    df_previsoes = fazer_previsoes(best_model, features, df)
    
main()
