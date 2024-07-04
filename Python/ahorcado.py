##########################
#palabras.py
##########################
# Importamos del módulo random, creamos una lista de palabras y con random.choice seleccionamos una palabra al azar:
import random
def seleccionar_palabra():
    palabras = ["python", "programacion", "ahorcado", "aprobaste", "computadora", "desarrollo", "proyecto"]
    return random.choice(palabras)
#############################
#diagramas.py
#############################
#Los hacemos una funcion para que cada elemento sea contado como un intento.
def mostrar_diagrama(intentos):
    diagrama = [
        '''
          ------
          |    |
          |
          |
          |
          |
        -------
        '''
        ,
        '''
          ------
          |    |
          |    O
          |
          |
          |
        -------
        '''
        ,
        '''
          ------
          |    |
          |    O
          |    |
          |
          |
        -------
        '''
        ,
        '''
          ------
          |    |
          |    O
          |   /|
          |
          |
        -------
        '''
        ,
        '''
          ------
          |    |
          |    O
          |   /|\\
          |
          |
        -------
        '''
        ,
        '''
          ------
          |    |
          |    O
          |   /|\\
          |   /
          |
        -------
        '''
        ,
        '''
          ------
          |    |
          |    O
          |   /|\\
          |   /\\
          |
        -------
        '''
    ]
    return diagrama[intentos]


#######################
#main.py
#######################
# import palabras
# import diagramas
#Si cada letra advinada esta en la palabra seleccionada, entonces se guarda en resultado, sino, se agrega un guion bajo. Nos devuelve el resultado. 
#Con el metodo strip lo añadimos
def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()
#Aqui mostramos las letras que no fueron de la palabra, con join añadimos cada letra con una coma para mas orden. 
def mostrar_letras_erradas(letras_erradas):
    return "Letras erradas: " + ", ".join(letras_erradas)
#Aqui es donde seleccionamos la palabra y ponemos en ejecucion el programa, creamos listas de letras erradas y adivinadas, contamos los intentos y declaramos el maximo de intentos de acuerdo a la funcion de los diagramas.
def ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    letras_erradas = []
    intentos = 0
#Aquí empezamos el juego con la interfaz del juego, empezamos bucle de todo con while True:
    while True:
        print("\n" + mostrar_diagrama(intentos))
        print("Palabra: " + mostrar_palabra(palabra_secreta, letras_adivinadas))
        print(mostrar_letras_erradas(letras_erradas))

        letra = input("Ingresa una letra: ").lower()
        #Verifica si la entrada de la letra es valida luego ve si esa letra esta en las letras adivinadas o en letras erradas, si es asi nos muestra que ya la usamos. 
        #La funcion isalpha nos ayuda a verificar si la letra es cadena y len si es solo un carácter. 
        if letra.isalpha() and len(letra) == 1:
            if letra in letras_adivinadas or letra in letras_erradas:
                print("Ya has ingresado esa letra.")
            if letra in palabra_secreta:
                letras_adivinadas.append(letra)
                #Verifica si todas las letras han sido adivinadas:
                #Después si la letra esta en la palabra secreta, la añade a letras adivinadas. 
                #Y si se completan todas las letras para la palabra secreta ganaste, el bucle se rompe
                if set(letras_adivinadas) == set(palabra_secreta):
                    print("\n¡Felicidades ganaste! Has adivinado la palabra: " + palabra_secreta)
                    break
                #Sino, se añaden a letras erradas y los intentos van sumando hasta llegar al maximo. Cuando llegas al maximo perdiste y te enseña la palabra secreta.
                #El bucle se rompe, son 6 diagramas por lo tanto 6 intentos.
            else:
                letras_erradas.append(letra)
                intentos += 1
            if intentos == 6:
                print("\nHas alcanzado el límite de intentos, perdiste. La palabra era: " + palabra_secreta)
                break
        else:
            print("Por favor, ingresa una letra válida.")

# Inicia el juego
ahorcado()
