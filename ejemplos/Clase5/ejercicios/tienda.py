class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def vender_producto(self, id_producto, cantidad):
        for producto in self.inventario:
            if producto.id == id_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                else:
                    return

    def generar_informe(self):
        texto = ""
        for producto in self.inventario:
            texto += f"Producto: {producto.nombre}, Precio de venta: {producto.precio_venta}, Stock: {producto.stock} \n"
        return texto
