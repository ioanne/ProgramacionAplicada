class Item:
    def __init__(self, data):
        self.accepts_mercadopago = data.get("accepts_mercadopago")
        self.address = Address(data.get("address"))
        self.attributes = [Attribute(attr) for attr in data.get("attributes")]
        self.available_quantity = data.get("available_quantity")
        self.buying_mode = data.get("buying_mode")
        self.catalog_listing = data.get("catalog_listing")
        self.catalog_product_id = data.get("catalog_product_id")
        self.category_id = data.get("category_id")
        self.condition = data.get("condition")
        self.currency_id = data.get("currency_id")
        self.differential_pricing = data.get("differential_pricing")
        self.discounts = data.get("discounts")
        self.domain_id = data.get("domain_id")
        self.id = data.get("id")
        self.installments = data.get("installments")
        self.inventory_id = data.get("inventory_id")
        self.listing_type_id = data.get("listing_type_id")
        self.official_store_id = data.get("official_store_id")
        self.official_store_name = data.get("official_store_name")
        self.order_backend = data.get("order_backend")
        self.original_price = data.get("original_price")
        self.permalink = data.get("permalink")
        self.price = data.get("price")
        self.promotions = data.get("promotions")
        self.sale_price = data.get("sale_price")
        self.seller = Seller(data.get("seller"))
        self.seller_address = SellerAddress(data.get("seller_address"))
        self.shipping = Shipping(data.get("shipping"))
        self.site_id = data.get("site_id")
        self.sold_quantity = data.get("sold_quantity")
        self.stop_time = data.get("stop_time")
        self.tags = data.get("tags")
        self.thumbnail = data.get("thumbnail")
        self.thumbnail_id = data.get("thumbnail_id")
        self.title = data.get("title")
        self.use_thumbnail_id = data.get("use_thumbnail_id")
        self.winner_item_id = data.get("winner_item_id")


class Address:
    def __init__(self, data):
        self.city_id = data.get("city_id")
        self.city_name = data.get("city_name")
        self.state_id = data.get("state_id")
        self.state_name = data.get("state_name")


class Attribute:
    def __init__(self, data):
        self.attribute_group_id = data.get("attribute_group_id")
        self.attribute_group_name = data.get("attribute_group_name")
        self.id = data.get("id")
        self.name = data.get("name")
        self.source = data.get("source")
        self.value_id = data.get("value_id")
        self.value_name = data.get("value_name")
        self.value_struct = data.get("value_struct")
        self.value_type = data.get("value_type")
        self.values = data.get("values")


class Seller:
    def __init__(self, data):
        self.car_dealer = data.get("car_dealer")
        self.car_dealer_logo = data.get("car_dealer_logo")
        self.id = data.get("id")
        self.nickname = data.get("nickname")
        self.permalink = data.get("permalink")
        self.real_estate_agency = data.get("real_estate_agency")
        self.registration_date = data.get("registration_date")
        self.seller_reputation = SellerReputation(data.get("seller_reputation"))
        self.tags = data.get("tags")


class SellerReputation:
    def __init__(self, data):
        self.level_id = data.get("level_id")
        self.metrics = data.get("metrics")
        self.power_seller_status = data.get("power_seller_status")
        self.transactions = data.get("transactions")


class SellerAddress:
    def __init__(self, data):
        self.address_line = data.get("address_line")
        self.city = City(data.get("city"))
        self.comment = data.get("comment")
        self.country = Country(data.get("country"))
        self.id = data.get("id")
        self.latitude = data.get("latitude")
        self.longitude = data.get("longitude")
        self.state = State(data.get("state"))


class City:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")


class Country:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")


class State:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")


class Shipping:
    def __init__(self, data):
        self.benefits = data.get("benefits")
        self.free_shipping = data.get("free_shipping")
        self.logistic_type = data.get("logistic_type")
        self.mode = data.get("mode")
        self.promise = data.get("promise")
        self.store_pick_up = data.get("store_pick_up")
        self.tags = data.get("tags")


diccionario = {
    "accepts_mercadopago": True,
    "address": {
        "city_id": None,
        "city_name": "Villa Celina",
        "state_id": "AR-B",
        "state_name": "Buenos Aires",
    },
    "attributes": [
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "BRAND",
            "name": "Marca",
            "source": 1,
            "value_id": "2503",
            "value_name": "Motorola",
            "value_struct": None,
            "value_type": "string",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "DETAILED_MODEL",
            "name": "Modelo detallado",
            "source": 3942444344910321,
            "value_id": "20081059",
            "value_name": "PAVU0003BR",
            "value_struct": None,
            "value_type": "string",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "GPU_MODEL",
            "name": "Modelo de GPU",
            "source": 3942444344910321,
            "value_id": "7498817",
            "value_name": "PowerVR GE8320",
            "value_struct": None,
            "value_type": "string",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "ITEM_CONDITION",
            "name": "Condición del ítem",
            "source": 1,
            "value_id": "2230284",
            "value_name": "Nuevo",
            "value_struct": None,
            "value_type": "list",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "LINE",
            "name": "Línea",
            "source": 3942444344910321,
            "value_id": "59187",
            "value_name": "Moto",
            "value_struct": None,
            "value_type": "string",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "MODEL",
            "name": "Modelo",
            "source": 1,
            "value_id": "22417731",
            "value_name": "Moto E22 4/64",
            "value_struct": None,
            "value_type": "string",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "PACKAGE_LENGTH",
            "name": "Largo del paquete",
            "source": 1,
            "value_id": None,
            "value_name": "17.6 cm",
            "value_struct": {"number": 17.6, "unit": "cm"},
            "value_type": "number_unit",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "PACKAGE_WEIGHT",
            "name": "Peso del paquete",
            "source": 1,
            "value_id": None,
            "value_name": "300 g",
            "value_struct": {"number": 300, "unit": "g"},
            "value_type": "number_unit",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "PROCESSOR_MODEL",
            "name": "Modelo del procesador",
            "source": 3942444344910321,
            "value_id": "12002613",
            "value_name": "Mediatek MT6765V/CB Helio G37",
            "value_struct": None,
            "value_type": "string",
            "values": [{...}],
        },
        {
            "attribute_group_id": "OTHERS",
            "attribute_group_name": "Otros",
            "id": "WEIGHT",
            "name": "Peso",
            "source": 3942444344910321,
            "value_id": None,
            "value_name": "169 g",
            "value_struct": {"number": 169, "unit": "g"},
            "value_type": "number_unit",
            "values": [{...}],
        },
    ],
    "available_quantity": 500,
    "buying_mode": "buy_it_now",
    "catalog_listing": True,
    "catalog_product_id": "MLA25665291",
    "category_id": "MLA1055",
    "condition": "new",
    "currency_id": "ARS",
    "differential_pricing": {"id": 35713384},
    "discounts": None,
    "domain_id": "MLA-CELLPHONES",
    "id": "MLA1471211850",
    "installments": {
        "amount": 26666.33,
        "currency_id": "ARS",
        "quantity": 3,
        "rate": 0,
    },
    "inventory_id": "FTWZ61238",
    "listing_type_id": "gold_pro",
    "official_store_id": 1938,
    "official_store_name": "Mercado Libre Electronica",
    "order_backend": 1,
    "original_price": 89999,
    "permalink": "https://www.mercadolibre.com.ar/moto-e22-64g-4gb-ram-azul/p/MLA25665291",
    "price": 79999,
    "promotions": [],
    "sale_price": None,
    "seller": {
        "_": False,
        "car_dealer": False,
        "car_dealer_logo": "",
        "id": 608846165,
        "nickname": "MERCADOLIBRE ELECTRONICA_AR",
        "permalink": "http://perfil.mercadolibre.com.ar/MERCADOLIBRE+ELECTRONICA_AR",
        "real_estate_agency": False,
        "registration_date": "2020-07-13T13:21:30.000-04:00",
        "seller_reputation": {
            "level_id": "5_green",
            "metrics": {
                "cancellations": {...},
                "claims": {...},
                "delayed_handling_time": {...},
                "sales": {...},
            },
            "power_seller_status": "platinum",
            "transactions": {
                "canceled": 50441,
                "completed": 766685,
                "period": "historic",
                "ratings": {...},
                "total": 817126,
            },
        },
        "tags": ["brand", "large_seller", "messages_as_seller"],
    },
    "seller_address": {
        "address_line": "",
        "city": {"id": None, "name": "Villa Celina"},
        "comment": "",
        "country": {"id": "AR", "name": "Argentina"},
        "id": None,
        "latitude": None,
        "longitude": None,
        "state": {"id": "AR-B", "name": "Buenos Aires"},
    },
    "shipping": {
        "benefits": None,
        "free_shipping": True,
        "logistic_type": "fulfillment",
        "mode": "me2",
        "promise": None,
        "store_pick_up": False,
        "tags": ["fulfillment", "mandatory_free_shipping"],
    },
    "site_id": "MLA",
    "sold_quantity": 500,
    "stop_time": "2043-08-18T13:20:10.000Z",
    "tags": [
        "good_quality_thumbnail",
        "deal_of_the_day",
        "extended_warranty_eligible",
        "ahora-3",
        "catalog_only_restricted",
        "immediate_payment",
        "cart_eligible",
        "best_seller_candidate",
        "shipping_guaranteed",
    ],
    "thumbnail": "http://http2.mlstatic.com/D_858094-MLU70795779606_082023-I.jpg",
    "thumbnail_id": "858094-MLU70795779606_082023",
    "title": "Moto E22 64g 4gb Ram Azul ",
    "use_thumbnail_id": True,
    "winner_item_id": None,
}


# a = Item(diccionario)
# print(a)
