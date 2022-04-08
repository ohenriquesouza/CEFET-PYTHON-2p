numero=(int(input("Entre com um número: ")))
cont=0
for n in range(1, numero+1):
    if numero % n == 0:
        cont += 1
if cont <= 2:
    print("O número inserido é primo.")
else:
    print("O número inserido não é primo.")