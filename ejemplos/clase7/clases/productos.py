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


# a = Item(diccionario)
# print(a)
