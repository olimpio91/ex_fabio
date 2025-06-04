entrada = int(input("Digite um numero: "))

while entrada < 0:
    entrada = int(input("Digite novamente: "))

for x in range(1, 11):
    print(f"{x} x {entrada} = {x * entrada}")