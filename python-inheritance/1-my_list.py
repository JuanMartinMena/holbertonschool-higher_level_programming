#!/usr/bin/python3
"""
Este módulo define una clase MyList que hereda de la clase list,
e incluye un método para imprimir la lista ordenada en orden ascendente.
"""


class MyList(list):
    """
    Clase que extiende la funcionalidad de la clase incorporada list.

    Métodos:
        print_sorted(self): Imprime la lista en orden ascendente.
    """

    def print_sorted(self):
        """
        Imprime la lista actual, pero en orden ascendente.

        La lista original no se modifica, solo se imprime una versión ordenada.
        """
        return sorted(self)
