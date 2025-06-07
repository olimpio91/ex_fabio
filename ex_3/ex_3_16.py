from os import system

valor = int(input("Digite um numero qualquer: "))
continuar = ''
resultado = 1

while True:
    
    
    if valor > 0:
        
        resultado *= valor
        valor = valor - 1
        continue

    if valor == 0:
        print(f"resultado: {resultado}")
        break

    else:
        print("\nvalor fornecido é negativo, digite um valor novamente!\n")
        continuar = input("Deseja continuar '[S]im' [N]ão:  ").lower()

        if continuar == "s":
            system("clear")
            valor = int(input("Digite um numero qualquer: "))
            continue
        else:
            break