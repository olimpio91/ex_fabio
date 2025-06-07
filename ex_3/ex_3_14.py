quantidade = int(input("Digite a quantidade de numeros: "))
valor = 0
maior_numero = 0
menor_numero = 0
soma_valores = 0
media = 0
quantidade_positivos = 0
quantidade_negativos = 0
por_positivos = 0
por_negativos = 0

if quantidade > 0 and quantidade <= 20:

    for i in range(quantidade):

        valor = int(input("Digite um valor qualquer: "))
        
        if valor > maior_numero:
            maior_numero = valor
        
        if valor < menor_numero:
            menor_numero = valor
        
        if valor > 0:
            quantidade_positivos += 1
        
        if valor < 0:
            quantidade_negativos += 1
        soma_valores += valor


por_positivos = (quantidade_positivos / quantidade) * 100
por_negativos = (quantidade_negativos / quantidade) * 100
media = soma_valores / quantidade

print(f"Maior numero : {maior_numero}")
print(f"Menor numero: {menor_numero}")
print(f"Soma dos valores: {soma_valores}")
print(f"Média {media}")
print(f"Porcentagem de positivos: {por_positivos}")
print(f"Porcentagem de negativos: { por_negativos}")