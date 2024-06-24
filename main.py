import random as rd


devine=rd.randint(0, 6)
print(f'voici la vrai valeur: {devine}')

def repete():
    nombre_deviner= int(input('veiller saisir la chiffre à deviner: '))
    return nombre_deviner


for i in range(3):
    repete()
    if repete == devine:
        print('vous avez gagner')
    else:
        print('ça va aller')