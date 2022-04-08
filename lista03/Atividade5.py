def conversao (hora, minuto):
    if(0< hora <= 12 and 0 < minuto < 60):
        print(f"{hora}:{minuto} AM")
    elif(12< hora < 24 and 0 < minuto < 60):
        print(f"{hora-12}:{minuto} PM")
hora=int(input("Informe as horas: "))
minuto=int(input("Informe os minutos: "))
conversao(hora, minuto)