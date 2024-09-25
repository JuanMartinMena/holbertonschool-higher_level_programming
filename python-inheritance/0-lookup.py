#!/usr/bin/python3
"""
Este módulo define la función lookup, que devuelve
la lista de atributos y métodos disponibles de un objeto.
"""


def lookup(obj):
    """
    Devuelve una lista de los atributos y métodos disponibles del objeto dado.

    Args:
        obj: El objeto a inspeccionar.

    Returns:
        list: Una lista de los atributos y métodos disponibles para el objeto.
    """
    return dir(obj)
