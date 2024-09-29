#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Inicializa el iterador
        self.count = 0  # Inicializa el contador

    def get_count(self):
        return self.count  # Devuelve el contador actual

    def __next__(self):
        try:
            item = next(self.iterator)  # Obtiene el siguiente elemento del iterador
            self.count += 1  # Incrementa el contador
            return item  # Devuelve el elemento
        except StopIteration:
            raise StopIteration  # Lanza StopIteration si no hay más elementos

