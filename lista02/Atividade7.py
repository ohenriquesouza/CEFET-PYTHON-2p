frase = str(input("Entre com uma frase: "))
cont = 0
for i in frase:
    if i == " ":
        cont += 1
    elif i == "\n":
        cont += 1
    elif i == "\t":
        cont += 1
print(f"'{cont +1}' palavras identificadas")
