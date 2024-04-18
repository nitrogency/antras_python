import json

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

from shop.shop_items import Food, Drink

class Customer:
    # identifikatorius, kuris leidzia atpazinti, kiek vartotoju yra ir kelintas
    # yra vartotojas
    identifier = 0

    def __init__(self, name, shopping_cart = None):
        # Inicijuojamas klientas su vardu ir pasirenkamu pirkinių krepšeliu. Jeigu krepšelis nusuteiktas, jis numatyta reikšmė tuščias masyvas.
        if not isinstance(name, str) or len(name) == 0: # patikrina, ar vardas yra ne skaicius ar kt. ir ar jis nera tuscias
            raise TypeError("Vardas turi buti tinkamo tipo ir ilgesnis uz 0") # jei taip, ismetama klaida
        self.__name = name  # nustatomas toks vardas klientui, koks buvo duotas konstruktoryje
        Customer.identifier += 1 # identifikatorius padidinimas sukurus nauja klienta
        self.identifier = Customer.identifier # identifikatoriaus reiksme priskiriama klientui

        if shopping_cart is None: # Jeigu krepšelis nusuteiktas, suteikiamas tuščias krepšelis.
            shopping_cart = []
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
    
    """
    Užduotis #5
        Pridėtos funkcijos: export_to_json (kliento duomenų eksportavimo funkcija į json failą)
        from_json (kliento duomenų importavimo funkcija iš json failo)

    Parametrai:
        customer_data: eksportuojami duomenys į json failą
        file_path: failo keliui nurodyti naudojamas kintamasis
        data: skirtas užkrauti importuojamus duomenis iš json failo

    Rezultatas:
        Programa leidžia eksportuoti kliento duomenis į json failą, kurį reikia susikurti pačiam.
        Taip pat programa leidžia nuskaityti ir importuoti kliento duomenis iš json failo.
    """
    # Duomenų eksportavimo į json failą metodas
    def export_to_json(self, file_path):
        
        customer_data = { # Visų eksportavimui reikiamų duomenų žodynas 
            "name": self.__name,
            "identifier": self.identifier,
            "items": [item.to_dict() for item in self.shopping_cart] # Praeina pro kiekvieną pirkinį pirkinių krepšelyje
        }

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(customer_data, file, indent=4, ensure_ascii=False) # Customer_data nurodo ką eksportuoti, file nurodo kur, indent=4 suformatuoja eksportuot1 tekstą iki keturių tarpelių (tab), ensure_ascii=False leidžia lietuviškas raides
        except Exception as e:
            print(f"Error: {e}")
    
    # Duomenų importavimo iš json failo metodas
    @classmethod
    def from_json(cls, file_path):
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file) # Užkrauna duomenis iš json failo

            name = data.get("name") # Gaunamas kliento vardas
            identifier = data.get("identifier") # Gaunamas kliento identifikatorius
            items_data = data.get("items", []) # Gaunamas pirkinių krepšelis

            # Sukuriamas naujas kintamasis perteikti kliento vardą bei indikatorių konsolėje
            customer = cls(name)
            customer.identifier = identifier

            # Praeinama pro kiekvieną pirkinį iš pirkinių krepšelio
            for item_data in items_data:
                item_name = item_data.get("name")
                quantity = item_data.get("quantity")
                price = item_data.get("price")
                full_info = item_data.get("full")

                # Nustatoma ar pirkinys yra Maistas ar Gėrimas
                if "Maistas" in full_info:
                    item = Food(item_name, quantity, price)
                else:
                    item = Drink(item_name, quantity, price)

                # Pirkinys pridedamas į kliento krepšelį
                customer.add_item(item)

            return customer # Grąžina surinktą informaciją apie klientą
        except FileNotFoundError: # Jeigu buvo nerastas failas, iš kurio importuoti, išspausdinamas pranešimas
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")
        return None
