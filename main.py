import random, numpy as np

numeros_escolhidos = []

for i in range(1,7):
    numeros_escolhidos.append(int(input(''+str(i)+ '° Número - Digite um número entre 1 e 60: ')))
numeros_escolhidos = sorted(numeros_escolhidos)
print('SEUS NUMEROS: ', numeros_escolhidos)
input('ENTER PARA COMEÇAR....')

acertos = 0

while acertos != 6:
    numeros_sorteados = random.sample(range(1,61), 6)
    numeros_sorteados = sorted(numeros_sorteados)
    print(numeros_sorteados)

    resultado = np.in1d(numeros_escolhidos, numeros_sorteados)
    acertos = len(np.intersect1d(numeros_escolhidos, numeros_sorteados))

    if resultado.all():
        print('PARABENS!!!! VOCE GANHOU')
        print('NUMEROS SORTEADOS: ', numeros_sorteados)
        print('SEUS NNUMEROS: ', numeros_escolhidos)