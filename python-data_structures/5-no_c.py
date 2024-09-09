#!/usr/bin/python3
def no_c(my_string):
    # Crear una lista vacía para almacenar los caracteres válidos
    new_string = []

    # Recorrer cada carácter en la cadena original
    for char in my_string:
        # Agregar el carácter a la lista solo si no es 'c' ni 'C'
        if char != 'c' and char != 'C':
            new_string.append(char)
    
    # Unir la lista en una nueva cadena
    return ''.join(new_string)
