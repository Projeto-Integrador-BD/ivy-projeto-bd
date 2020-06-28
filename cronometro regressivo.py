# exemplo de um contador regressivo que pode ajudar  a manter o foco na execução de tarefas
#será melhorado , será incluido um comando de voz para ativação e ampliada a capacidade de tempo.

from time import sleep


t= int(input("Quantos tempo irá dedicar a sua tarefa ? "))
for tempo in range(t,0,-1):
    sleep(t)
    if sleep(t) == sleep(8):
        print("Foco no trabalho!")
    if sleep(t) == sleep(6):
        print("Nem pense em mexer no whatsapp!")
    if sleep(t) == sleep(4):
        print("Continue assim!")
    if sleep(t) == sleep(2):
        print("Quase lá ! ")
    break
print("acabou!")