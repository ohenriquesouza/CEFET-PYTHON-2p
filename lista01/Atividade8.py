# Não consegui fazer esse exercício, fiquei em dúvida em relação a como printar o numero 'x' quando fosse detectado
# que ele é primo. Se puder corrigir essa em aula, seria muito bom #
numero=(int(input("Entre com um número: ")))
cont=0
for numero in range(1, numero):
    cont = 0
    for C in range (1, numero+1):
           if numero % C == 0:
               cont+=1
    if cont <= 2:
        print(f"Numero primo '{numero}' encontrado")