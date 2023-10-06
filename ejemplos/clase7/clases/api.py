import copy
import requests

from productos import Item


class MercadoLibreAPI:
    API = "https://api.mercadolibre.com"

    def __init__(self):
        self._products = []

    @property
    def products(self):
        return copy.deepcopy(self._products)

    def set_products(self, products):
        self._products = products

    @classmethod
    def get_url(cls, resource):
        return f"{cls.API}{resource}"

    def _get_products(self, resource):
        """resource: /sites/MLA/search?category=MLA1055"""
        url = self.get_url(resource)
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("results", [])

    def get_products(self, resource):
        products = []
        results = self._get_products(resource)
        for result in results:
            products.append(Item(result))
        self.set_products(products)
        return products

    def filter_products_by_attr(self, attr_name, attr_value):
        filtered_products = [
            producto
            for producto in self.products
            if self.has_attr(producto, attr_name, attr_value)
        ]
        return filtered_products

    def filter_products(self, products=None, start_price=None, end_price=None):
        """
        Start price y end price son obligatorios ambos
        Hay que mejorar los elif.
        """
        # Genero una copia profunda de la lista de productos
        filtered_products = []
        products = self.products if products is None else products
        for product in products:
            # Esto ya no es un diccionario, ahora es un objeto. reempĺazar product["price"] por product.price
            filter_start_price = start_price and product["price"] > start_price
            filter_end_price = end_price and product["price"] < end_price
            if filter_start_price and filter_end_price:
                filtered_products.append(product)
            elif start_price is not None and end_price is not None:
                continue
            elif filter_start_price:
                filtered_products.append(product)
            elif filter_end_price:
                filtered_products.append(product)
        return filtered_products

    def has_attr(self, producto, attr_name, attr_value):
        """Esto va dentro de Item"""
        # Esto ya no es un diccionario, ahora es un objeto.
        for atributo in producto.get("attributes", []):
            has_attr_name = atributo.get("name").lower() == attr_name.lower()
            has_attr_value = (
                atributo.get("value_name", "").lower() == attr_value.lower()
            )
            if has_attr_name and has_attr_value:
                return True
        return False


api = MercadoLibreAPI()
api.get_products("/sites/MLA/search?category=MLA1055")
zz = api._get_products("/sites/MLA/search?category=MLA1055")


results = api.filter_products_by_attr(attr_name="Marca", attr_value="Motorola")

results_1 = api.filter_products(products=results, start_price=20000, end_price=80000)
results_2 = api.filter_products(start_price=20000, end_price=80000)
results_3 = api.filter_products(start_price=20000)
results_4 = api.filter_products(products=results, start_price=20000)

print(results)
