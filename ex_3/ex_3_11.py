from fractions import Fraction

n = int(input("Digite um valor qualquer: "))

numerador = 1
denominador = 2 
soma = 0
while True:
    if n < 0 or n > 50:
        n = int(input("Digite um valor novamente: "))
    else:
        for i in range(1, n + 1):
            #print(i)

            soma += Fraction(numerador, denominador)

            numerador += 1
            denominador += 1
        break

print(soma)