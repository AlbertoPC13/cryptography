# Código de cifrado Vigeneré en Python

# Se obtiene del archivo de texto el mensaje a cifrar (M)
# Se requiere tener un archivo llamado 'message.txt'
file = open("message.txt", "r")

message = file.read()

print(f'\nMensaje original: {message}')

# Se obtiene la longitud del mensaje original
size = len(message) - 1

# Se valida que el mensaje tenga una longitud en el rango de [5,100]
if(size < 5 or size > 100):
    print(f'\n\nEl tamaño de mensaje debe estar en el rango de 5 a 100\n\n')
    exit()

print(f'\nTamaño del mensaje: {size}')

# Se crea una lista para representar el vector de llaves (K)
keys = []

while True:
        try:
            numKeys = int(input(f'\nIngresa el numero de llaves (claves) a usar en el cifrado: '))
        except ValueError:
            print(f'\nError: Solo se admiten valores numericos\n')
            continue

        if (numKeys >= 1 and numKeys <= size):
            break;
        else:
            print(f'\nError: El número de claves debe estar en el rango de 1 a {size}\n')

for i in range(numKeys):
    # Se solicita al usuario ingresar la clave del cifrado (K), 
    # se valida que sea un valor numérico en el rango de 0 a 25
    while True:
        try:
            key = int(input(f'\nIngresa el valor del desplazamiento (clave) {i}: '))
        except ValueError:
            print(f'\nError: Solo se admiten valores numericos\n')
            continue

        if (key >= 0 and key <= 25):
            keys.append(key)
            break;
        else:
            print(f'\nError: El valor de la clave debe estar en el rango de 0 a 25\n')

# Se crea una lista vacía para almacenar el mensaje cifrado
ciphered = []

keyIndex = 0

# Se recorre cada caracter en la cadena del mensaje original
for i in message:
    # Se comprueba si se ha llegado al valor tope de las llaves
    if(keyIndex == numKeys):
        keyIndex = 0
    # Se comprueba si se ha llegado al EOF
    if(i == '\n'):
        break;

    # Se omiten del cifrado los caracteres de espacio
    if (i == " "):
        ciphered.append(" ")
        continue

    # Se crea una variable para guardar el valor ASCII del caracter actual
    c = ""
    # Se crea una variable para diferenciar si el caracter corresponde a una mayúscula o minúscula 
    alphabet = ""

    # Se comprueba si el caracter actual corresponde a una letra mayúscula o minúscula
    if (ord(i) >= ord("a") and ord(i) <= ord("z")):
        c = ord(i) - ord("a")
        alphabet = ord("a")
    elif (ord(i) >= ord("A") and ord(i) <= ord("Z")):
        c = ord(i) - ord("A")
        alphabet = ord("A")

    # Se realiza el cifrado por medio de la función de desplazamiento
    ciphered.append(chr(((c + keys[keyIndex]) % 26) + alphabet))
    keyIndex = keyIndex + 1

# Se imprime el mensaje cifrado
print("\n\nMensaje cifrado: " + "".join(ciphered) + "\n")

# Se escribe el mensaje cirfado en un archivo de texto
file = open('cipheredMessage.txt','w')
file.write("".join(ciphered) + "\n")
file.close()