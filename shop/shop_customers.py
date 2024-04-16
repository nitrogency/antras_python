"""
    Užduotis #1
    Kliento klasė, leidžianti priskirti vardą bei automatiškai priskirianti
    jo identifikatorių. Taip pat leidžia šias reikšmes išspausdinti.
    
    Parametrai:
        identifier (int): Kliento identifikatorius. Didinamas su kiekvienu kartu,
        kai yra sukuriamas naujas klientas.
        __name: Privatus kliento vardas. Prieinamas tik iš klasės metodų.
        __identifier: Privatus kliento identifikatorius. Prieinamas tik iš klasės metodų.
"""

from shop_items import Food, Drink

class Customer:
    # identifikatorius, kuris leidzia atpazinti, kiek vartotoju yra ir kelintas
    # yra vartotojas
    identifier = 0

    def __init__(self, name, shopping_cart = []):
        # Inicijuojamas klientas su vardu ir pasirenkamu pirkinių krepšeliu. Jeigu krepšelis nusuteiktas, jis numatyta reikšmė tuščias masyvas.
        if not isinstance(name, str) or len(name) == 0: # patikrina, ar vardas yra ne skaicius ar kt. ir ar jis nera tuscias
            raise TypeError("Vardas turi buti tinkamo tipo ir ilgesnis uz 0") # jei taip, ismetama klaida
        self.__name = name  # nustatomas toks vardas klientui, koks buvo duotas konstruktoryje
        Customer.identifier += 1 # identifikatorius padidinimas sukurus nauja klienta
        self.identifier = Customer.identifier # identifikatoriaus reiksme priskiriama klientui
        self.shopping_cart = shopping_cart  # Pirkėjui priskiriamas pateiktas prekių krepšelis

    def full_info(self): # isspausdina visa informacija apie klienta
        return "Vardas: " + self.__name + " | " + str(self.identifier)

    def get_identifier(self): # grazina kliento identifikatoriu
        return self.identifier
    @property
    def get_name(self): # grazina kliento varda. @property reikalinga tam, nes 'name' kintamasis yra privatus. 'getter' metodas, grazinantis reiksme. 
        return self.__name
    @get_name.setter # funkcija, naudojama kliento vardo pakeitimui. 'setter' metodas, leidziantis pakeisti privacia reiksme.
    def set_name(self, name):
        self.__name = name

    """
    Užduotis #4
        Pridėtos funkcijos: add_item(), remove_item(), get_items() leidžia valdyti pirkinių krepšelį.

    Parametrai:
        shopping_cart (list): maisto ir gėrimų objektų, reprezentuojančių kliento pirkinių krepšelį, masyvas. Pagal default nustatymus sąrašas yra tuščias.
        item (Food, Drink): maisto arba gėrimo objektas, su kuriou yra atliekamas funkcijos veikla.
        
    Rezultatas:
        Programa palengvina klientų objektų kūrimą su galimybe valdyti pirkinių krepšelius su maisto ir gėrimų prekėmis. Ji palaiko prekių pridėjimą ir pašalinimą iš krepšelio ir suteikia galimybę gauti visų prekių sąrašą su jų informacija.
    """
    
    def add_item(self, item):  
        # Prekės įdėjimo į kliento pirkinių krepšelį metodas
        if not isinstance(item, (Food, Drink)):
            raise TypeError("Prekė turi būti maistas arba gėrimas")
        self.shopping_cart.append(item)  # Įdedama prekė į pirkinių krepšelį

    def remove_item(self, index):  
        # Prekės pašalinimo iš kliento krepšelio metodas
        try:
            del self.shopping_cart[index]  # Pašalinamas elementas nurodytame indekse
        except IndexError:
            print("Error removing item")

    def get_items(self):  
        # Metodas gauti visų pirkėjo pirkinių krepšelyje esančių prekių sąrašą
        return [item.full_info() for item in self.shopping_cart]