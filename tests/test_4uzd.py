import unittest
from shop.shop_customers import Customer
from shop.shop_items import Food, Drink

class TestCustomerShoppingCart(unittest.TestCase):
    def setUp(self): # Sukuriamas klientas prieš kiekvieną testą
        self.customer = Customer("Jonas Jonaitis")

    def test_add_item(self): # Tikrinama ar pridėtą prekė yra tarp kliento (Customer) krepšelio (shopping_cart)
        food = Food("Batonas", 2, 1.3)
        self.customer.add_item(food)
        self.assertIn(food, self.customer.shopping_cart)

    def test_remove_item(self): # Tikrinama ar prekė yra pašalinama iš kliento (Customer) krepšelio (shopping_cart)
        food = Food("Batonas", 2, 1.3)
        drink = Drink("CocaCola", 3, 1.7)
        
        self.customer.add_item(food)
        self.customer.add_item(drink)
        self.customer.remove_item(0)
        
        self.assertNotIn(food, self.customer.shopping_cart) # Tikrinama ar panaikinta prekė
        self.assertIn(drink, self.customer.shopping_cart) # Antras patikrinimas, ar nebuvo panaikinta kita prekė

    def test_remove_item_wrong_index(self): # Tikrinama ar neleidžiama panaikinti prekės indekse, kurio neegzistuoja
        self.customer.add_item(Food("Batonas", 2, 1.3))
        self.assertFalse(self.customer.remove_item(5))

    def test_get_items(self): # Tikrinama ar gražinta visų prekių informacija yra teisinga
        food = Food("Batonas", 2, 1.3)
        drink = Drink("CocaCola", 3, 1.7)
        
        self.customer.add_item(food)
        self.customer.add_item(drink)

        expected_info = [food.full_info(), drink.full_info()]
        self.assertEqual(self.customer.get_items(), expected_info)

if __name__ == '__main__':
    unittest.main()
