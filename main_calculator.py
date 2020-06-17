############################
# Calculadora Python - Ivy #
############################

#Passos

# 1 - Perguntar tipo de operação
# 2 - Perguntar primeiro número
# 3 - Perguntar segundo número
# 4 - Cálculo dos dois números
# 5 - Ivy Responde resultado

operacao = input("Qual operação (adição, subtração,multiplicação,divisão) você deseja fazer? ")
num1 = float(input("Pode falar o primeiro número: "))
num2 = float(input("Agora você pode falar o segundo número: "))

if operacao == 'adição':
    total = num1 + num2
    print("O Resultado é: ")
    print(total)
elif operacao == 'subtração':
    total = num1 - num2
    print("O Resultado é: ")
    print(total)
elif operacao == 'multiplicação':
    total = num1 * num2
    print("O Resultado é: ")
    print(total)
elif operacao == 'divisão':
    total = num1 / num2
    print("O Resultado é: ")
    print(total)
else:
    print("Calculo inválido, por favor fale qual operação deseja fazer")







