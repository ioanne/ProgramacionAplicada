class Movimiento:
    def __init__(self, velocidad, destreza):
        """Acá podían poner los atributos que querían"""
        self._velocidad = velocidad
        self.destreza = destreza

    @property
    def velocidad(self):
        return self._velocidad

    def incrementar_velocidad(self, valor):
        if valor >= self._velocidad:
            self._velocidad = valor


class Habilidad:
    def __init__(self, nombre, daño, tiempo_casteo):
        """Acá podían poner los atributos que querian"""
        self.nombre = nombre
        self.daño = daño
        self.tiempo_casteo = tiempo_casteo


class Equipo:
    def __init__(self, nombre, tipo, es_equipable, valor):
        """Acá podían poner los atributos que querian"""
        self.nombre = nombre
        self.tipo = tipo
        self.es_equipable = es_equipable
        self.valor = valor


class Personaje:
    # Configuración de la clase
    sub_clase = False

    def __init__(self, nombre, nivel, vida, mana):
        """Acá podían poner los atributos que querian"""
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.mana = mana
        self._velocidad_basica = 100
        self._destreza_basica = 50
        self.movimiento = Movimiento(
            velocidad=self._velocidad_basica + nivel,
            destreza=self._destreza_basica + nivel,
        )
        self.habilidad = Habilidad("Ataque básico", 10, 1.0)
        self.equipo = Equipo("Espada", "Arma", True, 20)

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre}")

    def usar_habilidad(self, habilidad, objetivo):
        """Abstracción, un método que no tiene implementación"""
        pass


class Orco(Personaje):
    """Aplicamos herencia"""

    def __init__(self, nombre, nivel, vida, mana):
        super().__init__(nombre, nivel, vida, mana)

    def atacar(self, enemigo):
        print(f"Golpea con un hacha a {enemigo.nombre}")


# Ejemplo de uso (esto no se pedia en el parcial)
mi_personaje = Personaje("Ejemplo", 1, 100, 50)
enemigo = Personaje("Enemigo", 1, 100, 50)
mi_personaje.movimiento.velocidad = 10
mi_personaje.usar_habilidad("Rayo", enemigo)
equipo = Equipo("Armadura", "ArmaduraCompleta", True, 30)
mi_personaje.equipo.equipar(equipo)
orco = Orco("Thrall", 5, 200, 50)
# Ejemplo del uso del de polimorfismo
orco.atacar(mi_personaje)
