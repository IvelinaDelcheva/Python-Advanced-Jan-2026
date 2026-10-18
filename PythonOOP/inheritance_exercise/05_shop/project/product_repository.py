from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Product | None:
        found_product = next((p for p in self.products if p.name == product_name), None)
        return found_product

    def remove(self, product_name):
        remove_product = self.find(product_name)
        if remove_product:
            self.products.remove(remove_product)

    def __repr__(self):
        return '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)
