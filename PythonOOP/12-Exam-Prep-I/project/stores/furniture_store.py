from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):

    def __init__(self, name: str, location: str):
        super().__init__(name, location, 50)

    @property
    def store_type(self):
        return "Furniture"

    def store_stats(self):
        store_info = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                      self.get_estimated_profit(),
                      f"**{self.store_type} for sale:"]
        furniture = {}
        for p in self.products:
            if p.model not in furniture:
                furniture[p.model] = {"num_of_product_pieces": 0, "price_per_model": 0}
            furniture[p.model]["num_of_product_pieces"] += 1
            furniture[p.model]["price_per_model"] += p.price

        sorted_furniture = dict(sorted(furniture.items(), key=lambda kv: kv[0]))
        for model, num_p_p in sorted_furniture.items():
            avg_price_per_model = num_p_p["price_per_model"] / num_p_p["num_of_product_pieces"]
            store_info.append(
                f"{model}: {num_p_p["num_of_product_pieces"]}pcs, average price: {avg_price_per_model:.2f}")

        return '\n'.join(store_info)
