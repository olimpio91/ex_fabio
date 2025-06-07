from os import system

quantidade = int(input("Digite a quantidade de numeros: "))
numero = 0
maior_numero = 0
menor_numero = 0
soma_valores = 0
media = 0
numeros_positivos = 0
numeros_negativos = 0
porcentagemP = 0
porcentagemN = 0
sair = ''

contador = 1
while True:
    
    
    if quantidade > 0 and quantidade < 20:    
        
        if contador <= quantidade:
        
            numero = int(input("Digite um numero:"))

            soma_valores += numero  
                
            if numero > maior_numero:
                maior_numero = numero

            if numero < menor_numero:
                menor_numero = numero
            
            if numero > 0:
                numeros_positivos += 1
            
            if numero < 0:
                numeros_negativos += 1
            
            contador += 1

            continue
        
        media = soma_valores / quantidade
        porcentagemP = (numeros_positivos / quantidade) * 100
        porcentagemN = (numeros_negativos / quantidade) * 100

        print(f"\nMaior Numero: {maior_numero}")
        print(f"Menor Numero: {menor_numero}")
        print(f"Soma dos valores: {soma_valores}")
        print(f"Média: {media}")
        print(f"Porcentagem de numeros positivos: {porcentagemP}")
        print(f"Porcentagem de numeros negativos:{porcentagemN}\n")
        
        sair = input("Você deseja Sair '[S]im' '[N]ão': ").lower()

        if sair == 's':
            break
        else:
            system("clear")
            quantidade = int(input("Digite a quantidade de numeros: "))
            

    else:
        print("Quantidade fornecida com valor negativo ou maior que o esperado, digite o valor novamente: ")
        quantidade = int(input("Digite a quantidade de numeros: "))