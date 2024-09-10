#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # Se asigna el valor de la primera key a best_key y el primer valor a best_value
    # items devuelve los pares key-value de a_dictionary
    # iter hace un objeto iterable en iterador esto es para poder recorrer el diccionario
    # next agarra la primera key y la iguala a best_key y el primer valor y lo iguala a best_value
    best_key, best_value = next(iter(a_dictionary.items()))
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    return best_key
