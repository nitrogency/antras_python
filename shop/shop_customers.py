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

class Customer:
    # identifikatorius, kuris leidzia atpazinti, kiek vartotoju yra ir kelintas
    # yra vartotojas
    identifier = 0

    def __init__(self, name): # konstruktorius, priimantis duota varda
        if not isinstance(name, str) or len(name) == 0: # patikrina, ar vardas yra ne skaicius ar kt. ir ar jis nera tuscias
            raise TypeError("Vardas turi buti tinkamo tipo ir ilgesnis uz 0") # jei taip, ismetama klaida
        self.__name = name # nustatomas toks vardas klientui, koks buvo duotas konstruktoryje
        Customer.identifier = Customer.identifier + 1 # identifikatorius padidinimas sukurus nauja klienta
        self.__identifier = Customer.identifier # identifikatoriaus reiksme priskiriama klientui

    def full_info(self): # isspausdina visa informacija apie klienta
        print("Vardas: " + self.__name + " | " + str(self.__identifier))

    @property
    def get_identifier(self): # grazina kliento identifikatoriu
        return self.__identifier
    @property
    def get_name(self): # grazina kliento varda. @property reikalinga tam, nes 'name' kintamasis yra privatus. 'getter' metodas, grazinantis reiksme. 
        return self.__name
    @get_name.setter # funkcija, naudojama kliento vardo pakeitimui. 'setter' metodas, leidziantis pakeisti privacia reiksme.
    def set_name(self, name):
        self.__name = name