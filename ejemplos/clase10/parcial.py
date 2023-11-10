class Movimiento:
    def correr(self):
        pass


class Equipo:
    pass


class Personaje:
    def __init__(self):
        self.movimiento = Movimiento()
        self._vida = 100

    def hablar(self):
        return "Hola, vengo a flotar"


class Habilidad:
    pass


class Orco(Personaje):
    def __init__(self):
        super().__init__()

    def hablar(self):
        return "Hola, soy un orco!"

    @property
    def vida(self):
        return self._vida

    def recibe_golpe(self, daño):
        if self.vida > 0:
            if daño > self.vida:
                self._vida = 0
            else:
                self._vida -= daño
        return self.vida


orco = Orco()


orco.recibe_golpe(100)
print(orco.vida)
