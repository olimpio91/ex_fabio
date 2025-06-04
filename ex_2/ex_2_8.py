from os import system
valores = []

lados = ["A", "B", "C"]
indice = 0
while len(valores) < 3:
    try:
        valores.append(int(input(f"Digite um valor para o lado {lados[indice]} do trinagulo: ")))
        if valores[indice] > 0:
            indice += 1
        else:
            print("Digite um valor maior que zero\n")
            valores.pop()

    except ValueError:
        print("Digite apenas numeros\n")

system("clear")
#desempacotamento
a,b,c = valores

if a + b > c :
    #Aprendi isso com o chat gpt, antes usava varios operadores lígicos
    #Esse tipo de comparação não sabia que era possivel.
    if a == b == c:
        print(f"Tringulo Equilatero: A = {valores[0]}, B = {valores[1]}, C = {valores[2]}")
    elif a == b or a == c or c == b:
        print(f"Triangulo Isósceles: A = {valores[0]}, B = {valores[1]}, C = {valores[2]}")
    else:
        print(f"Triangulo Escaleno: A = {valores[0]}, B = {valores[1]}, C = {valores[2]}")
else:
    print("Isso não é um triangulo")