"""
Conversão em Fahrenheit
"""
celcius = float(input(f'Insira em graus Cº para conversão em Fº :'))
#calculo
fahrenheit = celcius *(9.00 / 5.00) + 32.00  #formula de conversão de Cº para fahrenheit
print(f'Conversão= = {celcius} º é {fahrenheit}º.')
################################################################################################
"""
Conversão para Celsius
"""
fahrenheita = float(input(f'Insira em Fº para conversão em Cº'))
celciusa = 5.0 * (fahrenheita - 32.0) / 9.0 #formula de conversão de Fº para Celsius
print(f'Conversão de {fahrenheita} equivale a {celciusa}')
###############################################################################################
"""
Celcius para Kelvin
"""
kelvin = float(input(f'Insira em graus Kº para conversão em Cº :'))
celciusb = kelvin - 273.15
print(f'Conversão de {kelvin} equivale a {celciusb}')
###############################################################################################
"""
Kelvin para Celsius
"""
celsiusc = float(input(f' Insira em graus Cº para conversão em Kº'))
kelvinb = celsiusc + 273.15
print(f'Conversão de {celsiusc} equivale a {kelvinb}')