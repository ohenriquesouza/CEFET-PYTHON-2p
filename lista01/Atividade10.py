numero = str(input("Entre com um número: "))
iguais = 0
for c in range(len(numero)):
    if numero[c] == numero[-c-1]:
        iguais+=1
    if iguais == len(numero):
        print("É palindromo")     