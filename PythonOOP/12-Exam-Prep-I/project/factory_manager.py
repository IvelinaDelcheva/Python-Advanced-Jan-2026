from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        product_class = {"Chair": Chair, "HobbyHorse": HobbyHorse}.get(product_type)

        if not product_class:
            raise Exception("Invalid product type!")
        product = product_class(model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        store_class = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}.get(store_type)

        if not store_class:
            raise Exception(f"{store_type} is an invalid type of store!")
        store = store_class(name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store, *products):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        matching_sub_type = [p for p in products if p.sub_type in store.store_type]
        if not matching_sub_type:
            return "Products do not match in type. Nothing sold."
        store.products.extend(matching_sub_type)
        store.capacity -= len(matching_sub_type)
        self.income += sum(p.price for p in matching_sub_type)
        for p in matching_sub_type:
            self.products.remove(p)
        return f"Store {store.name} successfully purchased {len(matching_sub_type)} items."

    def unregister_store(self, store_name: str):
        unr_store = next((s for s in self.stores if s.name == store_name), None)
        if unr_store is None:
            raise Exception("No such store!")
        if unr_store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(unr_store)
        return f"Successfully unregistered store {unr_store.name}, location: {unr_store.location}."

    def discount_products(self, product_model: str):
        products_to_discount = [p for p in self.products if p.model == product_model]
        [p.discount() for p in products_to_discount]
        return f"Discount applied to {len(products_to_discount)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store_statistics = next((s for s in self.stores if s.name == store_name), None)
        if store_statistics is None:
            return "There is no store registered under this name!"
        return store_statistics.store_stats()

    def statistics(self):
        factory_info = [f"Factory: {self.name}",
                        f"Income: {self.income:.2f}",
                        "***Products Statistics***"
                        ]
        unsold_products = {}
        products_sum_price = 0.0
        for factory_p in self.products:
            if factory_p.model not in unsold_products:
                unsold_products[factory_p.model] = 0
            unsold_products[factory_p.model] += 1
            products_sum_price += factory_p.price
        factory_info.append(
            f"Unsold Products: {len(unsold_products.keys())}. Total net price: {products_sum_price:.2f}")
        for model in sorted(unsold_products.keys()):
            factory_info.append(f"{model}: {unsold_products[model]}")
        factory_info.append(f"***Partner Stores: {len(self.stores)}***")
        for s_store in sorted(self.stores, key=lambda store: store.name):
            factory_info.append(s_store.name)

        return '\n'.join(factory_info)
