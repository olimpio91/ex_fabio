from math import sin,cos,tan, pi

grau = int(float("Digite uma valor em graus: "))
anguloRadiano = grau * pi / 180

seno = sin(anguloRadiano)
coseno = cos(anguloRadiano)
tangente = tan(anguloRadiano)
secante = 1 / seno

print(f"seno: {seno} , coseno: {coseno} , tangente: {tangente} , secatnte: {secante}")