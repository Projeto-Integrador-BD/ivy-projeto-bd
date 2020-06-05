import random

lista_palavras = ["batata", "morango", "abacaxi"]
letras = ["a","b","c","d","e","f","g","i","j","k","l","m","n","o","p"]

gerar_palavras = True
gerar_numeros = True
gerar_0_9 = True
gerar_simbolos = False
gerar_abc = True
qtde_abc = 5
gerar_maiusculo = True

senha = ""

if gerar_palavras:
    valor = random.randint(0, 2)
    senha += lista_palavras[valor]
    
if gerar_numeros:
    if gerar_0_9:
        valor = random.randint(0, 9)
        senha += str(valor)

if gerar_abc:
    for i in range(qtde_abc):
        valor = random.randint(0, len(letras))
        senha += letras[valor]

print ("sua senha é: " + senha)
