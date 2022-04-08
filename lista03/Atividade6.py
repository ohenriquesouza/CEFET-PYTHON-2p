def valorPagamento (valor, atraso):
    if(atraso == 0):
        return valor
    else:
        return valor + ((3/100) * valor) + (((1/100) * valor) * atraso)  
valor=int(input("Informe o valor da prestação: "))
atraso=int(input("Informe a quantidade de dias de atraso: "))
print(f"Valor da prestação: R${valorPagamento(valor, atraso)}")