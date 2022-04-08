def contagem (numero):
    return len(str(numero))
numero=int(input("Informe um número inteiro: "))
print(f"O número digitado possui '{contagem(numero)}' dígitos")
