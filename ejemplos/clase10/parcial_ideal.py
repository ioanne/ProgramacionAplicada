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
        self._equipo = Equipo("Espada", "Arma", True, 20)

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre}")

    def usar_habilidad(self, habilidad, objetivo):
        """Abstracción, un método que no tiene implementación"""
        pass

    @property
    def equipo(self):
        return self._equipo

    def equipar(self, equipo: Equipo):
        if isinstance(equipo, Equipo):
            self._equipo = equipo
            print(f"Equipando {equipo.nombre} a {self.nombre}")

    def mostrar_info(self):
        pass


class Orco(Personaje):
    """Aplicamos herencia"""

    def __init__(self, nombre, nivel, vida, mana):
        super().__init__(nombre, nivel, vida, mana)

    def atacar(self, enemigo):
        print(f"Golpea con un hacha a {enemigo.nombre}")

    def usar_habilidad(self, habilidad, objetivo):
        """Implementación de un método abstracto"""
        print("Usando habilidad")

    def equipar(self, equipo):
        print(f"Orco {equipo.nombre} equipando a {self.nombre}")

    def mostrar_info(self):
        print("Mostrar info Orco")


class Elfo(Personaje):
    """Aplicamos herencia"""

    def __init__(self, nombre, nivel, vida, mana):
        super().__init__(nombre, nivel, vida, mana)

    def atacar(self, enemigo):
        print(f"Golpea con un hacha a {enemigo.nombre}")

    def mostrar_info(self):
        print("Mostrar info Elfo")


# Ejemplo de uso (esto no se pedia en el parcial)
mi_personaje = Personaje("Ejemplo", 1, 100, 50)
enemigo = Personaje("Enemigo", 1, 100, 50)
mi_personaje.movimiento.incrementar_velocidad(10)
mi_personaje.usar_habilidad("Rayo", enemigo)
equipo = Equipo("Armadura", "ArmaduraCompleta", True, 30)
mi_personaje.equipar(equipo)
orco = Orco("Thrall", 5, 200, 50)
# Ejemplo del uso del de polimorfismo
orco.atacar(mi_personaje)


personajes: list[Personaje] = [
    Orco("Orco1", 1, 123, 123),
    Orco("Orco2", 1, 123, 123),
    Elfo("Elfo", 1, 123, 123),
]


for personaje in personajes:
    personaje.usar_habilidad("Rayo", mi_personaje)
