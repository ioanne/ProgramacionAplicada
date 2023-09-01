class Movimiento:
    def __init__(self):
        self._corriendo = False

    def correr(self):
        self._corriendo = True
        return self._corriendo

    def caminar(self):
        self._corriendo = False
        return self._corriendo

    @property
    def esta_corriendo(self):
        """Propiedad publica para saber si esta corriendo."""
        return self._corriendo
