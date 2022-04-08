print("\n-----TODOS OS DADOS DEVERAM SER INSERIDOS NO FORMATO (dd/mm/aa)-----\n")
dia= int(input("Insira o dia do seu aniversário: "))
mes= int(input("O mês: "))
ano= int(input("O ano: "))
if (mes == 1):
    mes = 'Janeiro'
elif (mes == 2):
    mes = 'Fevereiro'
elif (mes == 3):
    mes = 'Março'
elif (mes == 4):
    mes = 'Abril'
elif (mes == 5):
    mes = 'Maio'
elif (mes == 6):
    mes = 'Junho'
elif (mes == 7):
    mes = 'Julho'
elif (mes == 8):
    mes = 'Agosto'
elif (mes == 9):
    mes = 'Setembro'
elif (mes == 10):
    mes = 'Outubro'
elif (mes == 11):
    mes = 'Novembro'
elif (mes == 12):
    mes = 'Dezembro'
else:
    print("Mês inválido.")
print(f"Você nasceu em: {dia} de {mes} de {ano}")