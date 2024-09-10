#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    # Iteramos sobre cada par clave-valor del diccionario original
    for key, value in a_dictionary.items():
        # Multiplicamos el valor por 2
        new_value = value * 2
        # Añadimos el nuevo par clave-valor al nuevo diccionario
        new_dictionary[key] = new_value
    return new_dictionary