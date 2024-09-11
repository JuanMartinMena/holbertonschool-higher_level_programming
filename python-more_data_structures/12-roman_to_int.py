#!/usr/bin/python3
def roman_to_int(roman_string):
    # Lo que tengo que hacer es recorrer el string y
    # que mientras que la letra de la izquierda sea de mayor valor
    # que la que esta en la derecha o igual se suman, sino se resta
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return None
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    valor_anterior = 0
    for simbolo in roman_string:
        valor_actual = valores[simbolo]
        if valor_actual > valor_anterior:
            total += valor_actual - 2 * valor_anterior
        else:
            total += valor_actual
        valor_anterior = valor_actual
    return total
