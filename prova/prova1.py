#Nome: Henrique Souza Fagundes
#Matrícula: 20213007196

import math
def q1():
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()
    print('Esse programa calcula o alcance e a altura de um projétil')
    nome_lancador=input('Nome do lançador: ')
    angulo_graus=float(input('Qual o ângulo de inclinação (em graus): '))
    velo_km=float(input('Qual a velocidade inicial (em km/h): '))
    g=9.81
    velo_ms=(velo_km)/3.6
    anguloRadianos=(angulo_graus * math.pi)/180 
    alcance=(pow(velo_ms,2)*math.sin(2*anguloRadianos))/g
    altura_max=(pow(velo_ms,2)*pow(math.sin(anguloRadianos),2))/(g*2)
    print('')
    print (f'{nome_lancador} fez lançamento com ângulo de {angulo_graus} graus e velocidade de {round(velo_ms, 2)} m/s.')
    print (f'A altura máxima foi de {round(altura_max, 2)} m.')
    print (f'A distância atingida foi de: {round(alcance, 2)} m.')



def q2():
# Escreva o código para a resolução da questão 2 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()
    print('Este programa calcula a velocidade de lançamento de uma bola de basquete')
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
    d1 = (-b + pow(D,(1/2)))/(2*a)
    d2 = (-b - pow(D,(1/2)))/(2*a)
    if(d1>0):
        aux=d1
    else:
        aux=d2
    print('')
    print(f'A bola deve ser lançada com velocidade inicial = {round(velocidade_ms,2)} m/s ou {round(velocidade_km,2)} km/h')
    print(f'Confirmando a cesta: para x = {distancia_cesta}m a bola estará a {round(confirma_altura_bola,2)}m !!!')
    print(f'Se não houvesse tabela, a bola tocaria o solo a {round(aux,2)}m da posição de lançamento.')
