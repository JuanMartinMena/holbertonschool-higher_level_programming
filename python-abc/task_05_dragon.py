#!/usr/bin/env python3

class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


# Para pruebas
if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()  # Debería imprimir: The creature swims!
    dragon.fly()   # Debería imprimir: The creature flies!
    dragon.roar()  # Debería imprimir: The dragon roars!
