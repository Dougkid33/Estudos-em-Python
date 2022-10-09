"""  Manipulando Strings
curso = 'pYtHon'
print(curso.upper())

print(curso.lower())

print(curso.title())

"""
# Funções de manipulação do tamanhi dos chars
nome = "DoUglAs"

print(nome.upper())
print(nome.lower())
print(nome.title())

# Funções de manipulação de espaços em branco
texto = "  Olá, mundo!! "
print(texto)
print(texto.strip() + ".")
print(texto.rstrip()+ ".")
print(texto.lstrip()+ ".")

#junções e centralização
menu = "Python"
print(menu.center(14, "#"))
print("-".join(menu))