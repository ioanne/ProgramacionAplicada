from categorias import Categoria, CategoriaRopa, CategoriaAccesorio, CategoriaCalzado


class Descuento:
    DESCUENTOS_POR_CATEGORIA = {
        CategoriaRopa.name: 10,
        CategoriaAccesorio.name: 12,
        CategoriaCalzado.name: 30,
        Categoria.name: 5,
    }  # Estos valores deberian venir de un setting

    @classmethod
    def obtener_descuento_por_categoria(cls, categoria):
        return cls.DESCUENTOS_POR_CATEGORIA.get(categoria.name)
