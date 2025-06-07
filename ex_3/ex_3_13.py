valores = []
maior_valor = 0
soma_valores = 0
media = 0

indice = 0
while len(valores) < 10:
    valores.append(int(input("Digite um valor: ")))

    if  valores[indice] > 0:
        
        if valores[0] > maior_valor:
            maior_valor = valores[indice]
        
        soma_valores += valores[indice]
        indice += 1
    else:
        print("Valor negativo, digite um valor novamente. \n")

media = soma_valores / len(valores)

print(maior_valor)
print(soma_valores)
print(media)