import os
os.system("clear")

Valor_A = int(input("Digite o valor A : "))
valor_B= int(input("Digite o valor B: "))
valor_C= int(input("Digite o valor C: "))

soma= Valor_A + valor_B < valor_C

if Valor_A + valor_B < valor_C:
    print("A + B > C!")
else:
    print("A + B < C!")