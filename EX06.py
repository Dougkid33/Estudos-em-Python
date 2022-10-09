"""
Exercicios do 10 ao 13
"""
# 10
# Ler velocidade em KM/H e converter para M/s
km_porhora = float(input(f'Insira a velocidade desejada em Km/h: '))
mts_segundos = km_porhora/3.6
print(f' A velocidade de {km_porhora} KM/H equivale a {mts_segundos} Mts/s.')

# 11
# Ler em M/s e converter para Km/H
mts_segundosb = float(input(f' Insira a velocidade em mt/s: '))
km_porhorab = mts_segundosb * 3.6
print(f' A velocidade de {mts_segundosb} Mts/s  equivale a {km_porhorab} KM/H.')

# 12
# Transformar Milhas para Km
milhas = float(input(f' Insira a velocidade em milhas: '))
km_porhorac = 1.61 * milhas
print(f' A velocidade de {milhas} convertida para Km/h é de {km_porhorac}')

# 13
# Transformar Km para Milhas
km_porhorad = float(input(f" Insira a velocidade em Km/h:"))
milhasb = km_porhorad / 1.61
print(f' A velocidade  {km_porhorad} Km/h  convertida para  {milhasb}')


