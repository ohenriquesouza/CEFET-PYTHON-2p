nome=str(input("Insira seu nome: "))
cont = len(nome)
while (cont >= 1):
    str = ''
    for j in range(0, cont):
        str += (nome[j])
    print(str)
    cont -= 1