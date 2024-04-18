import unittest
from shop.shop_items import Item

class TestItem(unittest.TestCase):

    def test_empty_name(self): # Tikrinama ar neleidžiama sukurti naują prekė su tuščiu pavadinimų
        with self.assertRaises(TypeError):
            Item("")

    def test_name_instance(self): # Tikrinama ar neleidžiama sukurti naują prekė su netinkamu pavadinimų
        with self.assertRaises(TypeError):
            Item(0)

    def test_quantity_instance(self): # Tikrinama ar neleidžiama sukurti naują prekė su netinkamu kiekių
        with self.assertRaises(TypeError):
            Item("Morkos", "du")

    def test_quantity_value(self): # Tikrinama ar neleidžiama sukurti naują prekė su neigiamų kiekių
        with self.assertRaises(ValueError):
            Item("Morkos", -1)

    def test_price_instance(self): # Tikrinama ar neleidžiama sukurti naują prekė su netinkama kaina
        with self.assertRaises(TypeError):
            Item("Morkos", price = "vienas")

    def test_price_value(self): # Tikrinama ar neleidžiama sukurti naują prekė su neigiama arba nuline kaina
        with self.assertRaises(ValueError):
            Item("Morkos", price = 0)

    def test_get_total_price(self): # Tikrinama ar tinkama suskaičiuojama visą prekių kiekio kaina
        item = Item("Pienas", 2, 1.5)
        self.assertEqual(item.get_total_price(), 3.0)

    def test_full_info(self): # Tikrinama ar full_info gražina teisingą informaciją
        item = Item("Pienas", 2, 1.5)
        self.assertEqual(item.full_info(), "Pienas 1.5 2 3.0")

    def test_to_dict(self):
        item = Item("Pienas", 2, 1.5) # Tikrinama ar to_dict gražina teisingą žodyną
        expected_dict = {'name': 'Pienas', 'quantity': 2, 'price': 1.5, 'total_price': 3.0, 'full': 'Pienas 1.5 2 3.0'}
        self.assertEqual(item.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
