import pandas as pd
import numpy as np
from datetime import date, timedelta

# Pedi sugestão ao Gemini
vendedores = ["Alice Pereira", "Bob Oliveira", "Charlie Souza", "David Silva"]
produtos = ["Viga de aco(Metro)", "Tijolo(Centena)", "Telha ceramica(Dezena)", "Cimento(Saca)", "Argamassa(Saca)"]
precos = [35, 80, 30, 55, 22.5]

# Criador de quantidade de vendas com pesos
def gerar_quantidade(q):
    
    intervalo = np.random.randint(1,11)

    # Coloquei esses números para a quantidade sorteada tender mais ao meio que aos extremos
    valor_somador = [0, 10, 10, 20, 20, 20, 30, 30, 40]
    somador_escolhido = np.random.choice(valor_somador)

    q = intervalo + somador_escolhido
    return q

# Definindo o intervalo de observação como o segundo trimestre de 2024
data_inicial = date(2024, 4, 1)  
data_final = date(2024, 6, 30) 

# Coloquei para gerar uma quantidade aleatoria de vendas no intervalo entre 150 e 300
num_linhas = np.random.randint(150, 300)

# Criei o data frame
df = pd.DataFrame(columns=["Data", "Vendedor", "Produto", "Quantidade", "Preço Unitário"])

# Criei a lista que irei adicionar cada venda 
linhas = []

# Gerador de vendas
for i in range(num_linhas):
    # Definir a data da respectiva venda
    data_venda = data_inicial + timedelta(days=np.random.randint((data_final - data_inicial).days + 1))

    # Definir o vendedor da respectiva venda
    vendedor = np.random.choice(vendedores)

    # Selecionar o índice que vai selecionar o produto e seu respectivo preço
    seletor_prod_prec = np.random.randint(0,5)
    produto = produtos[seletor_prod_prec]
    preco_unitario = precos[seletor_prod_prec]

    # Gerar a quantidade vendida daquele produto na respectiva venda
    quantidade = gerar_quantidade(q=0)

    # Inserir tudo na lista
    linhas.append({"Data": data_venda, "Vendedor": vendedor, "Produto": produto, "Quantidade": quantidade, "Preço Unitário": preco_unitario})

# Transforma a lista em um data frame
df = pd.DataFrame(linhas)

# Ordena pela data de venda, como se as vendas estivessem sendo adicionadas a cada dia
df = df.sort_values('Data', ascending=False)

# Cria o arquivo
df.to_csv("vendas.csv", index=False)