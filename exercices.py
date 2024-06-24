
# instruction de base 
# Exo1:
'''nom = input('veiller saisir votre nom: ')
age = int(input('veiller saisir votre age: '))
print(f"bonjour {nom}, tu as {age} ans et bienvenue à l'université") '''

#Exo2:
'''date_naissance = int(input('quelle est votre date de naissance : '))
print(f"merci beaucoup vous avez { 2024 - date_naissance} ans") '''

#Exo3:
'''L=int(input('veiller saisir la longueur: '))
l=int(input('veiller saisir la largeur: '))
print(f"le perimètre est égal à : {(L+l)*2}\n la surface est égal à {L *l} ") '''

#Exo4:
'''X = int(input('veiller saisir la valeur de X: '))
Y =int(input('veiller saisir la valeur de Y: '))
print(f"la puissance de Xy est de: {X**Y}") '''

#Exo5:
'''n1=4 ; n2=6
print(f"la somme de {n1} et {n2}:{n1 + n2}\n son produit est de {n1*n2}\n sa différence est {n1-n2}\n sa division est {n1/n2}") '''

#Exo6:
'''n1 = int(input('veiller saisir la note 1: '))
n2 = int(input('veiller saisir la note 2: '))
n3 = int(input('veiller saisir la note 3: '))
n4 = int(input('veiller saisir la note 4: '))
n5 = int(input('veiller saisir la note 5: '))
print(f"la somme est égale à : {n1+n2+n3+n4+n5}\n la moyenne est égale à {(n1+n2+n3+n4+n5)/5}")'''

#Exo7:
'''rayon = float(input('veiller saisir le rayon de la sphère: '))
print(f"le volume de cette sphère est égale à {(((4*3.14)*(rayon**3))/3):.2f}")'''

#Exo8:
'''A=int(input('saisir la valeur de A: '))
B=int(input('saisir la valeur de B: '))
A,B=B,A
print(f"la nouvelle valeur de A :{A} et celle de B :{B}") '''

#Exo9:
'''temps=int(input("veiller saisir le temps: "))

print(f"{temps//3600} heures {(temps % 3600)//60} minutes {(temps % 3600)%60} seconde") '''

#Exo10
'''from math import sqrt
Xa =float(input('veiller saisi Xa: '))
Xb =float(input('veiller saisi Xb: '))
Ya =float(input('veiller saisi Ya: '))
Yb =float(input('veiller saisi Yb: '))

print(f"la distace ={(sqrt((Xb -Xa)**2 + (Yb - Ya)**2)):.2f}") '''

#Exo11:
'''R1= float(input('valeur de R1: '))
R2= float(input('valeur de R2: '))
R3= float(input('valeur de R3: '))
print(f"la resistance en serie est {R1 + R2 + R3}, et celle en parallele est {((R1*R2*R3)/((R1*R2)+(R1*R3)+(R2*R3))):.2f}") '''


#                           les structures conditionnelles
#Exo12:
''' n1=2; n2=-5
if n1*n2 >=0:
    print(f"{n1} et {n2} sont de même signe")
else:
    print(f"{n1} et {n2} sont de signe opposé") '''

#Exo13:
'''n1=-2; n2=5
if n1*n2 >=0:
    n1,n2=n2,n1
    print(f"la nouvelle valeur de {n1 =} et celle {n2 =}")
else:
    print(f"la somme de n1 et n2 est de {n1 + n2} et le produit {n1*n2}") '''

#Exo14
'''nb=int(input('veiller saisir le nombre de photocopie: '))
if nb in range(9):
    print(f'le prix est égal à {nb * 0.3} dh')
elif nb in range(29):
    print(f'le prix est égal à {(10 * 0.3) + (nb -10)*0.25 } dh')
else:
    print(f'le prix est égal à {(10 * 0.3) + (20*0.25) + (nb - 30)*0.20} dh') '''

#Exo15:
''' age=int(input("veiller saisir l'age de l'enfant: "))
if  6 <= age <=7:
    print('poussin')
elif 8 <= age <=9:
    print("pipille")
elif 10 <= age <=11:
    print('minime')
elif 12 <= age: 
    print('kadet') '''

#Exo16:
