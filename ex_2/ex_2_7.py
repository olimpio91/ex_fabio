peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

relacao_Peso_altura = peso / altura ** 2

if relacao_Peso_altura < 20:
    print("Abaixo do peso")
elif relacao_Peso_altura < 25:
    print("Peso ideal")
else:
    print("Acima do peso")