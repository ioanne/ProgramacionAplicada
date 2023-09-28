from categorias import Categoria, CategoriaRopa, CategoriaAccesorio, CategoriaCalzado
from producto import Producto
from tienda import Tienda

categoria_electronica = Categoria("Electrónica")
categoria_ropa = CategoriaRopa("Ropa", "XL")
categoria_accesorio = CategoriaAccesorio("Pulsera de plata", 12, "Plata")
categoria_calzado = CategoriaCalzado("DC Pure", 43, "Negro")

producto1 = Producto(
    1,
    "Smartphone",
    "Teléfono inteligente avanzado",
    categoria_electronica,
    500,
    700,
    10,
)
producto2 = Producto(2, "Camisa", "Camisa de algodón", categoria_ropa, 20, 30, 50)
producto3 = Producto(3, "pulsera", "Pulsera", categoria_accesorio, 20, 30, 50)
producto4 = Producto(4, "zapa", "zapatilla", categoria_calzado, 20, 30, 50)

tienda = Tienda()
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.agregar_producto(producto4)


producto1.aplicar_descuento()
producto2.aplicar_descuento()
producto2.aplicar_descuento()
producto2.aplicar_descuento()

tienda.vender_producto(1, 3)

print(tienda.generar_informe())
