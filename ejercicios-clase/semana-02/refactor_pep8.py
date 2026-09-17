"""Módulo para el cálculo del promedio de una lista de números.

Aplica las convenciones de estilo PEP 8, anotaciones de tipos (type hints)
y estructura modular con punto de entrada main().
"""


def calcular_promedio(numeros: list[float]) -> float:
    """Calcula la media aritmética de una lista de números.

    Args:
        numeros: Lista con valores numéricos a promediar.

    Returns:
        Valor flotante que representa el promedio aritmético de los elementos.

    Raises:
        ValueError: Si la lista proporcionada está vacía.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía para calcular el promedio.")

    suma_total: float = 0.0
    for numero in numeros:
        suma_total += numero

    return suma_total / len(numeros)


def main() -> None:
    """Punto de entrada principal del script."""
    lista_ejemplo: list[float] = [1, 2, 3, 4, 5]
    promedio: float = calcular_promedio(lista_ejemplo)
    print(promedio)


if __name__ == "__main__":
    main()
