#!/usr/bin/python3
"""
Este módulo define una función que verifica si un objeto es una instancia
de una clase que hereda (directa o indirectamente) de la clase especificada.
"""

def inherits_from(obj, a_class):
    """
    Verifica si el objeto es una instancia de una clase que hereda de
    la clase especificada (directa o indirectamente).

    Args:
        obj: El objeto a verificar.
        a_class: La clase con la que se va a comparar.

    Returns:
        True si obj es una instancia de una clase que hereda de a_class,
        de lo contrario False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
