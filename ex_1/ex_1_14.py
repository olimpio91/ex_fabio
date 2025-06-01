
velocidadeInicial = int(input("Digite um valor para a velocidade Inicial em M/s: "))
acelerecao = int(input("Digite um valor para a aceleração em M/s²: "))
tempo = int(input("Digite um valor para o tempo do percurso em Segundos: "))

velocidadeFinal = (velocidadeInicial + acelerecao * tempo) * 3.6

print(f"A velocidade final do automovel: {velocidadeFinal}Km/h")
