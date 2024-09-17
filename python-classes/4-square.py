#!/usr/bin/python3
"""
Este módulo define una clase `Square` que representa un cuadrado.
"""


class Square:
    """
    Clase que define un cuadrado con un atributo privado de tamaño y métodos
    getter y setter para gestionar el acceso al tamaño.

    Atributos:
        __size (int): El tamaño del cuadrado.
    """

    def __init__(self, size=0):
        """
        Inicializa una nueva instancia de la clase Square.

        Args:
            size (int): El tamaño del cuadrado (opcional, valor por defecto 0).

        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Método getter para obtener el valor de `__size`.
        
        Returns:
            int: El tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Método setter para establecer el valor de `__size` con validación.

        Args:
            value (int): El nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2
