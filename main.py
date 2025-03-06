import csv


vendedores = ["Alice Pereira", "Bob Oliveira", "Charlie Souza", "David Silva"]

produtos = ["Viga de aco(Metro)", "Tijolo(Centena)", "Telha ceramica(Dezena)", "Cimento(Saca)", "Argamassa(Saca)"]

faturamento_vend = [0,0,0,0]
faturamento_prod = [0,0,0,0,0]

with open('vendas.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for linha in reader:
        data ,vendedor, produto, quantidade, preco = linha
        valor_total = int(quantidade) * float(preco)

        indice_v = vendedores.index(vendedor)
        indice_p = produtos.index(produto)

        faturamento_vend[indice_v] += valor_total
        faturamento_prod[indice_p] += valor_total
 
for i in range(len(produtos)):
    print(f"O total de vendas do produto {produtos[i]}, em Real, no segundo trimestre, foi R${faturamento_prod[i]}.\n")

maior_faturamento = max(faturamento_vend)
buscador = faturamento_vend.index(maior_faturamento)

print(f"O vendedor que obteve o maior faturamento foi {vendedores[buscador]} com um valor total de R${faturamento_vend[buscador]} em vendas!")
