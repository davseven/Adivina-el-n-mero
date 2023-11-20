#Adivina el numero
print ("¿TE SENTIS CON SUERTE HOY? ¡ADIVINA EN QUE NUMERO ESTOY PENSANDO!")
import random
jugar = True 

while jugar:
    numero = random.randint (1, 10)
    mi_numero = 0

    while mi_numero != numero:
        mi_numero = int (input ('ELIGE UN NUMERO ENTRE EL 1 Y EL 10: '))

        if (mi_numero < numero):
            print ('¡Intenta con un número mas alto!')
        elif (mi_numero > numero):
            print ('¡Intenta con un número mas bajo!')
        else:
            print ('¡ADIVINASTE! ¡FELICITACIONES!')

        
    if not input ('¿Queres jugar de nuevo? (si/no): ').lower () == 'si':
        break

print ("¡Nos vemos la próxima!¡SUERTE!")