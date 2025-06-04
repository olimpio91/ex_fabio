entrada = int(input("Digite um numero: "))
faixa = int(input("Digite até quanto sera calculado o seu numero: "))

while entrada < 0:
    entrada = int(input("Digite novamente: "))

while faixa <= entrada:
    faixa= int(input("Digite novamente até quanto sera calculado seu numero: "))

for x in range(1, faixa + 1):
    print(f"{x} x {entrada} = {x * entrada}")