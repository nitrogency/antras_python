"""
    Užduotis #2
    Programa turi klase prekėms. Prekės susidaro iš 3 kintamųjų: pavadinimo, kiekio ir kainos. 
    Sukuriant prekės objektą ir nepateikus prekės kiekio ar kainos, yra naudojamos numatytos reikšmės
    (kiekis - 1, kaina - 10). Prekės pavadinimas turi būti tekstas ir ne tusčias, kitaip iškeliamos klaidos.
    Su prekia galima atlikti 3 funckijas:
        get_total_price() - Gauti visos šios prekės kiekio kainą
        full_info() - Gauti visos šios prekės informacija tekstinių formatu
        to_dict() - Gauti visos šios prekės informacija žodyno formatu

    Parametrai:
        name (string): tekstas, kuris nurodo prekės pavadinimą.
        quantity (int): skaičius, kuris nurodo prekės kiekį.
        price (int): skaičius, kuris prekės vieneto kainą.
        
    Rezultatas:
        Programa sukuria prekių objektus ir gali atlikti visas ankščiau pabrėžtas funkcijas.

"""

class Item:
    def __init__(self, name, quantity = 1, price = 10): # Klasės konstruktorius, su numatytais parametrais
        if not name: # Tikrinama ar pavadinimas (name) nėra tusčias
            raise TypeError("Prekės pavadinimas negali būti tusčias")
        elif not isinstance(name, str): # Tikrinama ar pavadinimas yra tekstas
            raise TypeError("Prekės pavadinimas turi būti tekstas")

        if not isinstance(quantity, int): # Tikrinama ar kiekis yra sveikas skaičius
            raise TypeError("Prekės kiekis yra netinkamo tipo")
        elif quantity < 0: # Tikrinama ar kiekis nėra mažesnis už vieną
            raise ValueError("Prekės kiekis negali būti neigiamas")
        
        if not isinstance(price, float) and not isinstance(price, int): # Tikrinama ar kaina yra skaičius
            raise TypeError("Prekės kaina yra netinkamo tipo")
        elif price <= 0: # Tikrinama ar kaina nėra neigiama
            raise ValueError("Prekės kaina negali būti neigiama")

        self.name = name
        self.quantity = quantity
        self.price = price

    def get_total_price(self): # Gražina visų prekių kainą
        return self.quantity * self.price

    def full_info(self): # Sukuria ir gražina tekstą sudarytą iš prekės duomenų
        return "{} {} {} {}".format(self.name, self.price, self.quantity, self.get_total_price())

    def to_dict(self): # Sukuria ir gražina žodyną sudarytą iš prekės duoemenų
        return {"name": self.name,
                "quantity": self.quantity,
                "price": self.price,
                "total_price" : self.get_total_price()
                }

"""
    Užduotis #3
    Programa turi klases maisto ir gėrimo prekėms. Šios prekės paveldi viska iš prekės (Item) klasės, taigi turi tuos pačius parametrus
    ir funckijas, iškyrus viena - full_info(). full_info() yra redaguota tarp abudvieju klasiu, kad nurodytu ar prekė yra maistas ar
    gėrimas.

    Parametrai:
        Jokių naujų parametru nėra, taigi visi yra tie patys, kaip ir prekės (Item) klasėje.

        name (string): tekstas, kuris nurodo prekės pavadinimą.
        quantity (int): skaičius, kuris nurodo prekės kiekį.
        price (int): skaičius, kuris prekės vieneto kainą.
        
    Rezultatas:
        Su programa galima sukurti maisto ir gėrimų prekių objektus ir gali atlikti visas prekės funkcijas.
"""

class Food(Item): # Maisto (Food) klasė, kuri paveldi prekės (Item) klasę
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price) # Paveldima viskas iš prekės (Item) klasės
    
    def full_info(self): # Sukuria ir gražina tekstą sudarytą iš maisto prekės duomenų
        return "Maistas {} {} {} {}".format(self.name, self.price, self.quantity, self.get_total_price())

class Drink(Item): # Gėrimo (Drink) klasė, kuri paveldi prekės (Item) klasę
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price) # Paveldima viskas iš prekės (Item) klasės

    def full_info(self): # Sukuria ir gražina tekstą sudarytą iš gėrimo prekės duomenų
        return "Gėrimas {} {} {} {}".format(self.name, self.price, self.quantity, self.get_total_price())