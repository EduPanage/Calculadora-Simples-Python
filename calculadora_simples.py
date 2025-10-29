import time

print("\n\n--------------------------------Calculadora Simples--------------------------------\n\n")

def calculo (choice, num1, num2):
        if (choice == 1):
            return num1 + num2
        elif (choice == 2):
            return num1 - num2
        elif (choice == 3):
            return num1 * num2
        elif (choice == 4):
            if(num2 == 0):
                print("\nErro: Divisão por Zero")
            else:
                return num1 / num2
        else:
            return "Operação Inválida"

while True:

    choice = int(input("Escolha a operação desejada: \n\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\n\nSua Escolha: "))

    if (choice == 5):
        print("\n\nEncerrando Calculadora...\n\n")
        time.sleep(1)
        break

    else:
        num1 = int(input("Informe o primeiro numero: "))
        num2 = int(input("Informe o segundo numero: "))

        print("\nOperação Escolhida foi ",  choice)
        print("\n\nResultado: ", calculo(choice, num1, num2),"\n")
        time.sleep(2)
