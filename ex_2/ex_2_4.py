base = int(input("Digite um valor para a base do retangulo: "))
altura = int(input("Digite o valor da altura do retangulo: "))

area = base * altura
resposta = "Terreno grande" if area > 100 else None

print(resposta)