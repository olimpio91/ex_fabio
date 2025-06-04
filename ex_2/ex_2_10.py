from math import sqrt
ax2 = int(input("Digite o valor de A: "))
bx  = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = bx ** 2 - (4 * ax2 * c)

if delta > 0:
    x1 = -(bx * 2) + sqrt(delta) / 2 * ax2
    x2 = -(bx * 2) - sqrt(delta) / 2 * ax2

    if x1 == x2:
        print(f"Duas raízes iguais: {x1}, {x2}")
    else:
        print(f"Duas raízes : {x1}, {x2}")

else:
    print(f"Delta negativo: {delta}")