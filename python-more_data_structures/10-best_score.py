#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # items devuelve los pares key-value de a_dictionary
    # iter hace un objeto iterable en iterador
    # esto es para poder recorrer el diccionario
    # next agarra el siguiente key y valor
    # en este caso es el primer key y valor
    best_key, best_value = next(iter(a_dictionary.items()))
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    return best_key
