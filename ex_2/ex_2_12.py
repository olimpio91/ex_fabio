acelereca = float(input("Digite o valor da acelereção em m/s²: "))
velocidadeInicial = float(input("Digite o valor da velocidade inicial em m/s: "))
tempo = float(input("Digite o tempo do percurso em segundos"))

velocidadeFinal = (velocidadeInicial * acelereca * tempo) * 3.6

if velocidadeFinal < 40:
    print("Veículo muito lento")
elif velocidadeFinal < 60:
    print("Velocidade permitida")
elif velocidadeFinal < 80:
    print("Velocidade de cruzeiro")
elif velocidadeFinal < 120:
    print("Veículo rápido")
else:
    print("Veículo muito rápido")