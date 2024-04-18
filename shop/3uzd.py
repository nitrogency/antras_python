"""
    Užduotis #2
    Maisto (Food) ir Gėrimo (Drink) klasių naudojimas iš shop_items.py

    Parametrai:
        f1 (Food): pirmoji maisto prekė.
        f2 (Food): antra maisto prekė.
        d1 (Drink): pirmoji gėrimo prekė.
        d2 (Drink): antra gėrimo prekė.
        
    Rezultatas:
        Programa sukuria nurodytus maisto ir gėrimo prekių objektus ir atlieka klasių funkcijas full_info().
"""

from shop.shop_items import Food, Drink

f1 = Food("Batonas", 2, 1.3)
f2 = Food("Sviestas", 1, 1.3)

d1 = Drink("CocaCola", 3, 1.7)
d2 = Drink("Sprite", 2, 1.7)

print(f1.full_info())
print(f2.full_info())
print(d1.full_info())
print(d2.full_info())
