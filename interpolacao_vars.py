"""
Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, 
a segunda é utilizando o método format e a última é utilizando f strings.
A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, 
por esse motivo iremos focar nas 2 últimas.

"""

PI = 3.14159
print(f'valor de PI: {PI:.2f}')
print(f'valor de PI: {PI:10.2f}') # aqui a numeração antes do ponto se refere ao tanto de distancia
nome = "Doug the Kid"
idade = 27
profissao = "Programador"
linguagem = "Python"

print(f" Olá, meu nome é {nome}, tenho {idade} anos, pretendo me tornar {profissao} e estudo {linguagem}.")