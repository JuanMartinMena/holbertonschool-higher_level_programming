#!/usr/bin/python3
"""
Este módulo define una clase `Square` que representa un cuadrado.
"""


class Square:
    """
    Clase que define un cuadrado
    con atributos privados de tamaño y posición, métodos
    getter y setter, y métodos para
    calcular el área y para imprimir el cuadrado.

    Atributos:
        __size (int): El tamaño del cuadrado.
        __position (tuple): La posición
        de inicio de la impresión del cuadrado.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa una nueva instancia de la clase Square.

        Args:
            size (int): El tamaño del
            cuadrado (opcional, valor por defecto 0).
            position (tuple): La posición
            del cuadrado (opcional, valor por defecto (0, 0)).

        Raises:
            TypeError: Si size no es un
            entero o position no es una tupla de 2 enteros positivos.
            ValueError: Si size es menor que 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Método getter para obtener el valor de `__position`.

        Returns:
            tuple: La posición del cuadrado.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Método setter para establecer el valor de `__position` con validación.

        Args:
            value (tuple): La nueva posición del cuadrado.

        Raises:
            TypeError: Si value no es una tupla de 2 enteros positivos.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime el cuadrado en la consola usando el carácter `#`.
        Si el tamaño es 0, imprime una línea vacía.
        La posición afecta la cantidad de espacios y saltos de línea previos.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
