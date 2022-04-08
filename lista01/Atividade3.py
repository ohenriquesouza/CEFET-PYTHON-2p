qnt_salsicha=(int(input(("Informe a quantidade de salsichas ingeridas: "))))
qnt_anos=(int(input("Por quantos anos segue essa rotina?: ")))
vida_perdida= (((qnt_salsicha * 36) / 60) / 24) * (52 * qnt_anos) 
print("A quantidade de dias de vida perdido(s) foram: %d" %(vida_perdida))