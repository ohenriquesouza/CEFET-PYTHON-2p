nome=str(input("Insira seu nome: "))
for i in range(1, len(nome) +1):
    str = ''
    for j in range(0, i):
        str += (nome[j])
    print(str)