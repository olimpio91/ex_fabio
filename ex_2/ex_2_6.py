valores = []

print("Digite três valores inteiros logo abaixo\n")

while len(valores) < 3:
    valores.append(int(input("Digite um valor: ")))

maiorNumero = 0

for x in valores:
    if x > maiorNumero:
        maiorNumero = x

print(f"O maior valor: {maiorNumero}")