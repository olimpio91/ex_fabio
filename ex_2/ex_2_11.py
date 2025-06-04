peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu genero: ").lower()

calculo = peso / altura ** 2

if sexo == "masculino":
    if calculo < 20:
        print(f"Abaixo do peso: {calculo}")
    elif calculo < 25:
        print(f"Peso ideal: {calculo}")
    else:
        print(f"Acima do peso: {calculo}")
elif sexo == "feminino":
    if calculo < 19:
        print(f"Abaixo do peso: {calculo}")
    elif calculo < 24:
        print(f"Peso ideal: {calculo}")
    else:
        print(f"Acima do peso: {calculo}")