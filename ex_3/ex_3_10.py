
n = int(input("Digite um numero qualquer: "))
soma = 0

while True:
    if n < 0 or n > 100:
        n = int(input("Digite um numero novamente: "))
    else:
        # n² + 1, sendo que n é o numero do usuário
        for i in range(1, n + 1):
            soma += i ** 2 + 1
        break

print(soma)