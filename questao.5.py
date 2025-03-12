import os
os.system("clear")

primeiro_numero =int(input("digite um numero: "))
operador = input("digite a operação que deseja (+  * /): ")
segundo_numero =int(input("digite um numero: "))

match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado ="opção invalida."

print(f"Primeiro numero: {primeiro_numero}")
print(f"operação: {operador}")
print(f"segundo numero: {segundo_numero}")
print(f"resultado: {resultado}")