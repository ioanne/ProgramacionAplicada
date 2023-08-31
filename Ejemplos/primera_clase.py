# Creando una clase
class Auto:
    """Documentacion de mi clase."""

    # Creamos una constante con los valores rojo, verde y azul
    COLORES_VALIDOS: tuple = ("rojo", "verde", "azul")

    def __init__(self, marca: str, color: str, rodado: int):
        """Inicializamos los valores
        para empezar a trabajar con nuestra clase.
        """
        self.marca = marca
        self._color = color
        self.rodado = rodado

    def cambiar_color(self, color: str) -> str:
        """Creamos un metodo para editar el color
        que es una variable privada"""
        se_cambio_el_color = False
        if self.validar_color(color):
            self._color = color
            se_cambio_el_color = True
        return se_cambio_el_color

    @classmethod
    def validar_color(cls, color: str) -> bool:
        return color in cls.COLORES_VALIDOS

    @property
    def color(self) -> str:
        return self._color

    @staticmethod
    def metodo_estatico():
        pass


auto = Auto("Ford", "Rojo", 26)

# Accedemos a un método estatico para usarlo sin instanciar la clase.
print(Auto.validar_color("verde"))

# Accedemos a un método de la instancia para cambiar el color
print("Se cambio el color" if auto.cambiar_color("bordo") else "No se cambio el color")


print(auto.marca)
print(auto.color)
print(auto.rodado)
