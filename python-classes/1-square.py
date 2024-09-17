#!/usr/bin/python3
"""
Este módulo define una clase `Square` que representa un cuadrado.
"""


class Square:
    """
    Clase que define un cuadrado con un atributo privado de tamaño.
    
    Atributos:
        __size (int): El tamaño del cuadrado.
    """

    def __init__(self, size):
        """
        Inicializa una nueva instancia de la clase Square.
        
        Args:
            size (int): El tamaño del cuadrado.
        """
        self.__size = size
