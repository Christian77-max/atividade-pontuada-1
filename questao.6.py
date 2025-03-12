import os
os.system("clear")

primeira_nota = float(input("digite sua primeira nota: "))
segunda_nota = float(input("digite sua primeira nota: "))



soma = primeira_nota + segunda_nota
média = soma/2

print(f"média: {media}")

if média >= 6:
    print("parabens!") 
elif 4 <= media < 6:
    print("recuperação!")
if média < 4:
    print("reprovado!") 

print("media") 