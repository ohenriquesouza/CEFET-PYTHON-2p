n=(int(input("Entre com um número: ")))
b = 2
p = (b +(n/b))/2
qp = p ** 2
# print(f"b {b}")
# print(f"\np {p}") 
# print(f"\nqp {qp}")
while(abs(n - qp) >= 0.0001):
    b = p
    p = (b +(n/b))/2
    qp = p ** 2
print(f"A raiz é: {p}")