#!/usr/bin/python3
"""
Este módulo define una función que verifica si un objeto es una instancia
de una clase o de una clase que hereda de la clase especificada.
"""

def is_kind_of_class(obj, a_class):
    """
    Verifica si el objeto es una instancia de la clase especificada o
    de una clase que hereda de la misma.

    Args:
        obj: El objeto a verificar.
        a_class: La clase con la que se va a comparar.

    Returns:
        True si obj es una instancia de a_class o de una clase que hereda
        de a_class, de lo contrario False.
    """
    return isinstance(obj, a_class)
