# media = p1 + 2 * p2 / 3 = 5
#  p1 + 2 * p2 = 15
#  p2 = 15 - 2 -p1
#  2 * p2 = 15 - p1
# p2 = 15 - p1 / 2

p1 = float(input("Digite sua nota da primeira avalição: "))
p2 = (15 - p1) / 2

print(f"Você precisa tirar '{p2}' para passar de ano!")