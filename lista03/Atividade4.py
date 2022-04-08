def somaImposto (custo, imposto):
    return custo + ((imposto / 100) * custo)
custo=int(input("Informe o valor de custo do produto: "))
imposto=float(input("Insira o valor de imposto cobrado: "))
print(f"Valor corrigido: R${somaImposto(custo, imposto)}")