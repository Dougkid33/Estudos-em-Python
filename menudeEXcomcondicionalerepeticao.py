"""
Exercicio com condicionais e repetição mesclados para fixação
"""
opc = 0
menu = f'''
    ============ Menu de exercicios===============
    1 - Digite dois números, e verifique qual o maior:
    2 - Mostra os cinco primeiros  múltiplos de 3 maior que 0 :
    3 - Média da nota do aluno: 
    4 - Ordem crescente: 
    5 - Verificação do triangulo: 
    6 - SAIR.
'''
while opc != 6:
    print(menu)
    opc = int(input('Digite a opção desejada: '))
    if opc == 1:
        num1 = int(input('Insira o primeiro número: '))
        num2 = int(input('Insira o primeiro número: '))
        if num1 > num2:
            print(f' O número {num1} é maior que {num2}')
        elif num2 > num1:
            print(f' O número {num2} é maior que {num1}')
        else:
            print(' Os números são iguais')
    elif opc == 2:
        for numero in range(1, 18, 3):
            print(numero)
    elif opc == 3:
        nota1 = float(input(f' Insira a primeira nota: '))
        nota2 = float(input(f' Insira a segunda nota: '))
        nota3 = float(input(f' Insira a terceira nota: '))
        nota_peso_dois = nota3 * 2
        media = nota1 + nota2 + nota_peso_dois / 2
        if media < 6:
            print(' Aluno Reprovado!!!')
        elif media == 6:
            print(' Aluno de recuperação.')
        else:
            print(' Aluno aprovado!')
    elif opc == 4:
        numero2 = int(input(' Insira um nro :'))
        for nro in range(1, numero2):
            print(nro)
    elif opc == 5:
        ladoA = float(input(' Insira o lado A do triângulo: '))
        ladoB = float(input(' Insira o lado B do triângulo: '))
        ladoC = float(input(' Insira o lado C do triângulo: '))
        somaA = ladoA + ladoB
        if ladoA > somaA and ladoB > somaA and ladoC > somaA:
            print('Um lado não pode ser maior que a soma dos outros dois , tente novamente!!!')
        else:
            if ladoA == ladoB and ladoA == ladoB and ladoB == ladoC:
                print(' Aqui temos um triângulo EQUILÁTERO. ')
            elif ladoA != ladoB and ladoA != ladoC and ladoC == ladoB:
                print(' Triangulo isosceles!')
            elif ladoB != ladoA and ladoB != ladoC and ladoA == ladoC:
                print(' Triangulo isósceles!')
            elif ladoC != ladoA and ladoC != ladoA and ladoA == ladoB:
                print(' Triangulo isósceles!')
            else:
                print(' Triangulo escaleno!')
    else:
        opc = 6

