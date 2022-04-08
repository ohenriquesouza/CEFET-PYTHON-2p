print("Informe a velocidade atual do veiculo: ")
velocidade = int(input())
if velocidade > 60:
    print("Voce excedeu o limite de velocidade e foi multado.")
    multa = (velocidade - 60) * 5
    print(f"Valor da multa aplicada: R${multa}")
else:   
    print("Velocidade compativel com o trecho")