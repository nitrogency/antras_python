"""
    Užduotis #2
    Item klasės naudojimas iš shop_item.py

    Parametrai:
        i1 (Item): pirmoji prekė.
        i2 (Item): antroji prekė.
        i3 (Item): trečioji prekė.
        
    Rezultatas:
        Programa sukuria nurodytus prekių objektus ir atlieka Item klasės funkcijas full_info() ir to_dict().
"""

import shop_items

i1 = shop_items.Item("Morkos")
i2 = shop_items.Item("Pienas", 2, 1.5)
i3 = shop_items.Item("Batonas", price=0.5)

print(i1.full_info())
print(i2.full_info())
print(i3.full_info())

print(i1.to_dict())
print(i2.to_dict())
print(i3.to_dict())