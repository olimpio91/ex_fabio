valueOne = int(input("Digite um valor qualquer: "))
valueTwo = int(input("Digite outro valor qualquer: "))

maior = valueOne if valueOne > valueTwo else valueTwo

if valueOne == valueTwo:
    print("Os numeros são idênticos")
else:
    print(maior)