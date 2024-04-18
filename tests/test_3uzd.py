import unittest
from shop.shop_items import Item, Food, Drink

class TestFoodAndDrink(unittest.TestCase):

    def test_food_inheritance(self): # Tikrinama ar maisto (Food) klasė paveldi iš prekės (Item) klasės
        self.assertTrue(issubclass(Food, Item))

    def test_food_full_info(self): # Tikrinama ar maisto (Food) full_info gražina teisingą informaciją
        food = Food("Batonas", 2, 1.3)
        self.assertEqual(food.full_info(), "Maistas Batonas 1.3 2 2.6")

    def test_drink_inheritance(self): # Tikrinama ar gėrimo (drink) klasė paveldi iš prekės (Item) klasės
        self.assertTrue(issubclass(Drink, Item))

    def test_drink_full_info(self): # Tikrinama ar gėrimo (Drink) full_info gražina teisingą informaciją
        drink = Drink("CocaCola", 3, 1.7)
        self.assertEqual(drink.full_info(), "Gėrimas CocaCola 1.7 3 5.1")

if __name__ == '__main__':
    unittest.main()