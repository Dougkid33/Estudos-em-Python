"""
Ex do 14 ao 18 Guppe -  medidas
para formatação com casas decimais usar :.2 ou o numero de casas desejadas
"""

pi = 3.14
# Graus para radianos EX 14
graus = float(input('Insira os graus em radianos: '))
radianos = graus * pi / 180
print(f' {graus:.2} graus º equivale a {radianos:.2} radianos.')


# Radianos para Graus EX 15

radianos1 = float(input('insira quantidade em radianos: '))
graus1 = radianos * 180/pi
print(f' {radianos1:.2} radianos º equivale a {graus1:.2} graus º .')


# Polegada para Cm EX 16

polegada = float(input(' Insira a medida em polegadas: '))
cm = polegada * 2.54
print(f' o quantitativo {polegada:.2} em polegadas equivale a {cm:.2} cm. ')

# centímetros para polegada EX 17

cm1 = float(input(' Insira a medida em centímetros: '))
polegada1 = cm1/2.54
print(f'A quantidade de {cm1:.2} cm equivale a {polegada1:.2} polegadas.')

# metros cúbicos para Litros EX 18
metros_cubicos = float(input('Insira o valor em mts³: '))
litros = 1000 * metros_cubicos
print(f'A quantidade de {metros_cubicos:.2} mts³ equivale a {litros:.2} litros.')

# Litros para M³ EX 19
litros1 = float(input('Insira o valor em litros: '))
metros_cubicos1 = litros1 /1000
print(f'A quantidade de {litros1:.2} Lts equivale a {metros_cubicos1:.2} m³.')

# Kg para libras Ex 20
quilogramas = float(input(' Insira a quantidade em Kgs: '))
libras = quilogramas / 0.45
