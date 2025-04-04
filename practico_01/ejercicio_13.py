"""Clousures, Generadores, Generadores Delegados

Esta guia muestra uno de los patrones avanzados de programación para evitar
el uso de variables globales. El método descripto se llama closure y consiste
en vincular una función con datos que persistan luego de la ejecución, sin
recurrir a variables globales. Esto se hace mediante la declaración de una
función dentro de otra y permite comportamiento que sería imposible lograr de
otra manera.
"""


from typing import Iterator, Callable


def generar_pares_clousure(initial: int = 0) -> Callable[[], int]:
    """Toma un número inicial y devuelve una función que cada vez que es
    invocada devuelve el número par siguiente al devuelto la última vez que
    fue invocada.

    Restricciones:
        - Usar closures
        - Usar el modificador nonlocal
    """
    
    def inner() -> int:
        nonlocal initial
        initial += 2
        return initial
    return inner


# NO MODIFICAR - INICIO
generador_pares = generar_pares_clousure(0)
#assert generador_pares() == 0
assert generador_pares() == 2
assert generador_pares() == 4
# NO MODIFICAR - FIN



###############################################################################


"""Este tipo de comportamiento es conocido com semi-corutina, las semi-corutinas
en Python son llamadas funciones generadoras y se caracterizan por utilizar el
yield en lugar del return.
"""


def generar_pares_generator(initial: int = 0) -> Iterator[int]:
    """Re-Escribir utilizando Generadores
    Referencia: https://docs.python.org/3/howto/functional.html?highlight=generator#generators
    """
    while True:
        yield initial
        initial += 2


# NO MODIFICAR - INICIO
generador_pares = generar_pares_generator()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4
# NO MODIFICAR - FIN


###############################################################################


def generar_pares_generator_send(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando send para saltear numeros"""
    while True:
        x = yield initial
        if x is not None:
            initial = x #Si se detecta un send, setear initial
        else:
            initial += 2 #Si no, continuar como se esperaria


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_generator_send()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
    assert generador_pares.send(10) == 10
    assert next(generador_pares) == 12
    assert next(generador_pares) == 14
    assert next(generador_pares) == 16
# NO MODIFICAR - FIN


###############################################################################


def generar_pares_delegados(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando Generadores delegados (yield from)"""
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_delegados()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
# NO MODIFICAR - FIN
