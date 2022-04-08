import math

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