inicio = int(input("Digite um número: "))
fim = int(input("Digite o segundo número: "))

print("Números pares no intervalo:")

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(numero)