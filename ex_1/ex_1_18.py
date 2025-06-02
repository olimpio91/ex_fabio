produtos = []

item = 1
while len(produtos) < 5:
    produtos.append(float(input(f"Digite o valor do produto {item}: ")))
    item += 1

somaDosProdutos = sum(produtos)
print(f"Total : {somaDosProdutos}")

valor = float(input("Digite o valor referente ao pagamento: "))
troco = somaDosProdutos - valor

print(f"Dinheiro recebido: {valor}\nTroco: {troco}")


