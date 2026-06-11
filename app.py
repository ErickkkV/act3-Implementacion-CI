def areaTriangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Args:
        base (float): Base del triángulo.
        altura (float): Altura del triángulo.

    Returns:
        float: Área calculada.

    Raises:
        ValueError: Si la base o altura son menores o iguales a cero.
    """

    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero.")

    return (base * altura) / 2


if __name__ == "__main__":
    try:
        base = float(input("Base del Triángulo: "))
        altura = float(input("Altura del Triángulo: "))

        area = areaTriangulo(base, altura)

        print("Área del Triángulo:", area)

    except ValueError as e:
        print("Error:", e)
    
