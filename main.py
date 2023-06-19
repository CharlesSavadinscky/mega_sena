import random
from twilio.rest import twilio

numeros_escolhidos = []

while True:
    for i in range(1,7):
        numeros_escolhidos.append(int(input("Digite um número de 1 a 60: ")))

    
    print(numeros_escolhidos)
