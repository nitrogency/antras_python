
from shop.shop_customers import Customer
from shop.shop_items import Food, Drink

c1 = Customer("Jonas Jonaitis", [Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c1.export_to_json("tmp/c1.json")

c1 = Customer.from_json("tmp/c1.json")
print(c1.full_info())
print(c1.get_items())
