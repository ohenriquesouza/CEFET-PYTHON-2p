import math

nome_robo=input('Nome do robô lançador: ')
altura_robo=float(input('Qual a altura do robô lançador (em metros)?: '))
distancia_cesta=float(input('Qual a distância da cesta (em metros)?: '))
g=9.81
velocidade_ms=math.sqrt((-g*pow(distancia_cesta,2))/(3.05-distancia_cesta-altura_robo))
velocidade_km=velocidade_ms*3.6
alcance=(pow(velocidade_ms,2)/g)
altura_max=(pow(velocidade_ms,2)/(g*4))
confirma_altura_bola=((-g/pow(velocidade_ms,2))*pow(distancia_cesta,2)+distancia_cesta+altura_robo)
a=(-g/pow(velocidade_ms,2)) 
b=1
c=altura_robo
D = (pow(b,2)-4*a*c)
x1 = (-b + pow(D,(1/2)))/(2*a)
x2 = (-b - pow(D,(1/2)))/(2*a)
if(x1>0):
    aux=x1
else:
    aux=x2
print('')
print(f'A bola deve ser lançada com velocidade inicial = {round(velocidade_ms,2)} m/s ou {round(velocidade_km,2)} km/h')
print(f'Confirmando a cesta: para x = {distancia_cesta}m a bola estará a {round(confirma_altura_bola,2)}m !!!')
print(f'Se não houvesse tabela, a bola tocaria o solo a {round(aux,2)}m da posição de lançamento.')