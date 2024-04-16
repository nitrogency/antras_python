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