lista = []
print("Digite abaixo o valor das suas 4 notas ")
prova = 1

while len(lista) < 4:
    lista.append(float(input(f"Digite o valor da Prova {prova}: ")))
    prova += 1

media = sum(lista) / 4

print(f"Sua média: {media}")