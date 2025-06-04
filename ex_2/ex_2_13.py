p1 = float(input("Digite sua nota da avaliação 1: "))
p2 = float(input("Digite sua nota da  avaliação 2: "))

media = (p2 + 2 * p2) / 3

resultado = "Aprovado" if media >= 5 else "Reprovado"

print(resultado, media)