a = int(input("Digite o valor do lado A: "))
b = int(input("Digite o valor do lado B: "))
c = int(input("Digite o valor do lado C: "))

hipotenusa = 0
cateto1 = 0
cateto2 = 0

if a > b and a > c:
    hipotenusa = a
    cateto1 = b
    cateto2 = c

elif b > a and b > c:
    hipotenusa = b
    cateto1 = a
    cateto2 = c

elif c > a and c > b:
    hipotenusa = c
    cateto1 = a
    cateto2 = b

teorema ="É triangulo retangulo" if hipotenusa ** 2 == (cateto1 ** 2) + (cateto2 ** 2) else "Não é triangulo retangulo"

print(teorema, 'cateto A = ', cateto1,',', 'cateto B = ', cateto2)