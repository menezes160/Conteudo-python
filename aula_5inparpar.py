numero = int(input("digite um numero inteiro aleatório:"))

resto = numero % 2

if resto == 1:
    print("O valor",numero,"é impar")
else:
    print("O valor",numero,"é par")