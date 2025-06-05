p1, p2, p3 = 1, 1, 1

print(p1)
print(p2)
print(p3)


for i in range(17):
    proximo = p1 + p2 + p3

    p1 = p2
    p2 = p3
    p3 = proximo
    print(p3)