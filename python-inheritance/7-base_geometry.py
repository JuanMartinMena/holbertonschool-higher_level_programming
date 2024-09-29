#!/usr/bin/python3
"""
Este módulo define una clase BaseGeometry.
"""


class BaseGeometry:
    """
    Clase BaseGeometry que define métodos de geometría.
    """

    def area(self):
        """
        Método que calcula el área.
        Lanza una excepción indicando que el método no está implementado.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valida que el valor sea un entero mayor que 0.

        Args:
            name: El nombre del parámetro a validar.
            value: El valor a validar.

        Raises:
            TypeError: Si value no es un entero o si es un booleano.
            ValueError: Si value es menor o igual a 0.
        """
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
