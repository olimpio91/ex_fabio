from math import pi
height = int(input("Digite o valor da altura do cone : "))
raio = int(input("Digite o valor do raio do cone: "))

volume = (height * pi * raio ** 2) // 3

print(f"Volume do cone: {volume}")