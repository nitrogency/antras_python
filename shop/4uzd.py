"""
    Užduotis #4
    Programą sudaro maisto ir gėrimų klasės, taip pat klientų klasė. Kiekvienoje prekių klasėje yra pavadinimo, kiekio ir kainos 
    atributai, taip pat metodai, skirti apskaičiuoti bendrą kainą ir generuoti suformatuotą informacijos eilutę. 
    Klientų klasė valdo pirkinių krepšelį, leidžiantį pridėti ir išimti maisto ir gėrimų prekes. 

    Parametrai:
        - name (string): nurodo kliento vardą ir pavardę.
        - shopping_cart (list, optional): maisto ir gėrimų objektų, reprezentuojančių kliento pirkinių krepšelį, sąrašas. Pagal default nustatymus sąrašas yra tuščias.
        
    Rezultatas:
        Programa palengvina klientų objektų kūrimą su galimybe valdyti pirkinių krepšelius su maisto ir gėrimų prekėmis. Ji palaiko prekių pridėjimą ir pašalinimą iš krepšelio ir suteikia galimybę gauti visų prekių sąrašą su jų informacija.
"""

from shop_customers import Customer
from shop_items import Food, Drink

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