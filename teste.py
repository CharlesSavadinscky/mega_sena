import random

def sortear_numeros(qtd_numeros):
    numeros = random.sample(
        range(1,61),qtd_numeros
    )

    return sorted(numeros)

def realizar_sorteio():
    print("Sorteio dos numeros foi: ")
    qtd_numeros = 6
    numeros_sorteados = sortear_numeros(qtd_numeros)
    print("numeros sorteados")
    for numero in numeros_sorteados:
        print(numero)
    
realizar_sorteio()