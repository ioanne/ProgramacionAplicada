class FiguraGeometrica:
    def calcular_area(self):
        pass


class Rectangulo(FiguraGeometrica):
    """Clase que hereda de FiguraGeometrica y agrega base y altura en el inicializador.
    Además implementa el método calcular_area.
    No estamos utilizando clases abstractas."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Circulo(FiguraGeometrica):
    """Clase que hereda de FiguraGeometrica y agrega radio en el inicializador."""

    PI = 3.141592653589793

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return self.PI * self.radio**2


rectangulo = Rectangulo(5, 10)
circulo = Circulo(4)

print(rectangulo.calcular_area())
print(circulo.calcular_area())
