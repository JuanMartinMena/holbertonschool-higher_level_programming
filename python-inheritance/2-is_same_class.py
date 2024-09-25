#!/usr/bin/python3
"""
Este módulo define una función que verifica si un objeto es exactamente
una instancia de la clase especificada.
"""


def is_same_class(obj, a_class):
    """
    Verifica si el objeto es exactamente una instancia de la clase.

    Args:
        obj: El objeto a verificar.
        a_class: La clase con la que se va a comparar.

    Returns:
        True si obj es exactamente una instancia de a_class, de lo contrario False.
    """
    return type(obj) is a_class
