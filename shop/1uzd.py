from shop.shop_customers import Customer

c1 = Customer("Jonas Jonaitis")
c2 = Customer("Petras Petraitis")
c3 = Customer("Lukas Lukauskas")

print(Customer.identifier)

print(c1.get_identifier())
print(c2.get_identifier())
print(c3.get_identifier())

print(Customer.identifier)

print(c1.full_info())
