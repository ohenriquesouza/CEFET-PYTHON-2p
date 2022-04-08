valor_casa=(float(input("Valor da casa: R$")))
salario=(float(input("Insira seu salário: R$")))
tempo=(int(input("Em quantos anos pagará?: ")))
valor_total= valor_casa + valor_casa * 0.10
prestacao = valor_total / (tempo * 12)
print(f"Valor total da casa: R${valor_total}")
if(prestacao > (salario * 0.30)):
    print("Valor da prestação inválido.")
else:
    print(f"Cada prestação te custará: R${prestacao}")