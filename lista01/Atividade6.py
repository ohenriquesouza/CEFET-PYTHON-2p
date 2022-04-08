tipo=str(input("Insira seu tipo de instalação (R, I ou C): "))
consumo=(int(input("Insira seu consumo mensal em Kwh: ")))
if (tipo == "R") and consumo <= 500:
    print("Valor pago será de: R$%.0f" %(consumo * 0.40))
if (tipo == "R") and consumo > 500:
    print("Valor pago será de: R$%.0f" %(consumo * 0.65))
if (tipo == "C") and consumo <= 1000:
    print("Valor pago será de: R$%.0f" %(consumo * 0.55))
if (tipo == "C") and consumo > 1000:
    print("Valor pago será de: R$%.0f" %(consumo * 0.60))
if (tipo == "I") and consumo <= 5000:
    print("Valor pago será de: R$%.0f" %(consumo * 0.55))
if (tipo == "I") and consumo > 5000:
    print("Valor pago será de: R$%.0f" %(consumo * 0.60))