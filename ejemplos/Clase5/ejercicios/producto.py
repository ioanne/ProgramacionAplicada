from descuento import Descuento


class Producto:
    def __init__(
        self, id, nombre, descripcion, categoria, precio_compra, precio_venta, stock
    ):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock

    # No esta tan bueno, deberia estar en la tienda.
    def aplicar_descuento(self):
        descuento = Descuento.obtener_descuento_por_categoria(self.categoria)
        self.precio_venta -= self.precio_venta * (descuento / 100)
