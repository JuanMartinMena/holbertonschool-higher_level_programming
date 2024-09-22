#!/usr/bin/python3
"""
Este módulo define una clase Rectangle que representa un rectángulo.
"""


class Rectangle:
    """
    Clase que define un rectángulo con ancho y altura privados.
    También mantiene un conteo de instancias y un símbolo para la representación.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Inicializa el rectángulo con ancho y altura opcionales.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Obtiene el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Establece el ancho con validaciones.
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
        Establece la altura con validaciones.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcula el área del rectángulo.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcula el perímetro del rectángulo.
        Si el ancho o la altura es 0, retorna 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retorna una representación en forma de cadena del rectángulo.
        Utiliza el símbolo especificado para imprimir el rectángulo.
        Si el ancho o la altura es 0, retorna una cadena vacía.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ])

    def __repr__(self):
        """
        Retorna una representación oficial del rectángulo que permite
        recrear la instancia usando eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Mensaje de despedida al eliminar la instancia del rectángulo."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
