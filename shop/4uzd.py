"""
    Užduotis #4
    Kliento (Customer) iš shop_customers.py, Maisto (Food) ir Gėrimo (Drink) iš shop_items.py, naudojimas prekių krepšelyje.

    Parametrai:
        c1 (Customer) - pirmasis klientas.
        c2 (Customer) - antrasis klientas.
        
    Rezultatas:
        Programa prideda nurodytus klientus su jų prekių krepšelias. Yra atspausdinami jų prekės iš krepšelių ir atliekamos įvairios funckijos keičiant krepšelius.
"""

from shop.shop_customers import Customer
from shop.shop_items import Food, Drink

# Pavyzdinis panaudojimas:
c1 = Customer("Jonas Jonaitis", [Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c2 = Customer("Petras Petraitis", [Food("Sviestas", 1, 1.3), Drink("Sprite", 2, 1.7)])

print(c1.get_items()) # Atspausdinamos prekės 1 kliento pirkinių krepšelyje
print(c2.get_items()) # Atspausdinamos prekės 2 kliento pirkinių krepšelyje

c1.add_item(Drink("Fanta", 10, 1.7)) # Prideda gėrimą į 1 kliento pirkinių krepšelį
print(c1.get_items()) # Atspausdina atnaujintas prekes 1 kliento pirkinių krepšelyje

c2.remove_item(2) # Pašalina prekę (2) iš 2 kliento pirkinių krepšelio
c2.remove_item(1) # Pašalina kitą prekę (1) iš 2 kliento pirkinių krepšelio
print(c2.get_items()) # Spausdina atnaujintas prekes 2 kliento pirkinių krepšelyje
