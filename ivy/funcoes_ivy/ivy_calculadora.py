
from util import audio

def calcular(ivy):
            ivy.falar('Informe o primeiro numero')
            num1 = float(ivy.ouvir(False))
            ivy.falar('Informe o segundo numero')
            num2 = float(ivy.ouvir(False))
            ivy.falar('Ok, agora me diga qual operação deseja realizar? somar, subtrair, mutiplicar ou dividir?')
            operacao = ''
            while(operacao == '' or operacao not in ['somar','subtrair','mutiplicar','dividir', 'cancelar']):
                operacao = ivy.ouvir(False)

            if 'somar' in operacao:
                total = num1 + num2
                ivy.falar('O resultado é: '+str(total))
            if 'subtrair' in operacao:
                total = num1 - num2
                ivy.falar('O resultado é: '+str(total))
            if 'multiplicar' in operacao:
                total = num1 * num2
                ivy.falar('O resultado é: '+str(total))
            if 'dividir' in operacao:
                total = num1 / num2
                ivy.falar('O resultado é: '+str(total))

