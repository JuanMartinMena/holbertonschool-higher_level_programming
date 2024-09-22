#!/usr/bin/python3
"""
Este módulo define una clase Rectangle que representa un rectángulo.
"""


class Rectangle:
    """
    Clase que define un rectángulo con ancho y altura privados.
    """

    def __init__(self, width=0, height=0):
        """
        Inicializa el rectángulo con ancho y altura opcionales.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Establece el ancho del rectángulo con validaciones.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene la altura del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Establece la altura del rectángulo con validaciones.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
