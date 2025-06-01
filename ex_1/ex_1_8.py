from math import pi
raio = int(input("Digite o valor do raio da esfera: "))
aresta = int(input("Digite o valor da aresta do cubo: "))

volumeEsfera = (4 * pi * raio ** 3) // 3
volumeQuadrado = aresta ** 3

volumeLivre = volumeQuadrado - volumeEsfera

print(f"Volume livre: {volumeLivre}")