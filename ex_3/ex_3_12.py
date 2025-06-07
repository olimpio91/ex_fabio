from fractions import Fraction

n = int(input("Digite um valor: "))

numerador = 0
denominador = 0
soma = 0

indice = 1
while True:

    if n > 0 and n < 50:

        if indice <= n:

            numerador = indice ** 2 + 1
            denominador = indice ** 3
            soma += Fraction(numerador, denominador)
            indice += 1
            continue
        break
    else:
        n = int(input("Valor negativo ou maior que cinquenta, digite um valor novamente: \n"))
        
        

print(soma)