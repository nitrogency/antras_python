import unittest
from unittest.mock import patch, mock_open
import json
from shop.shop_customers import Customer
from shop.shop_items import Food, Drink

class TestCustomerJson(unittest.TestCase):
    def setUp(self): # Sukuriamas klientas prieš kiekvieną testą
        self.customer = Customer("Jonas Jonaitis", [(Food("Batonas", 2, 1.3)), Drink("CocaCola", 3, 1.7)])

    def test_export_to_json(self):
        expected_json = json.dumps({
            "name": "Jonas Jonaitis",
            "identifier": self.customer.get_identifier(),
            "items": [item.to_dict() for item in self.customer.shopping_cart]
        }, indent=4, ensure_ascii=False) # Sukuriamas teisingas json failo tekstas, tikrinimo tikslams

        mocked_open = mock_open() # Atidaromas failo testavimo failo srautas
        with patch('builtins.open', mocked_open):
            self.customer.export_to_json("tmp/c1.json.json")

        mocked_open.assert_called_with("tmp/c1.json.json", 'w', encoding='utf-8') # Tikrinama ar failas buvo atidarytas
        
        handle = mocked_open() # Išsaugoma failo rankena (Handle)
        
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list) # Sukuriamas testuojama failo tekstas
        self.assertEqual(written_data, expected_json) # Lyginami json tekstai

    def test_from_json(self):
        json_data = json.dumps({
            "name": "Jonas Jonaitis",
            "identifier": 1,
            "items": [
                {"name": "Batonas", "quantity": 2, "price": 1.3, "total_price": 2.6, "full": "Maistas Batonas 1.3 2 2.6"},
                {"name": "CocaCola", "quantity": 3, "price": 1.7, "total_price": 5.1, "full": "Gėrimas CocaCola 1.7 3 5.1"}
            ] # Sukuriamas teisingas json failo tekstas, tikrinimo tikslams
        })

        with patch('builtins.open', mock_open(read_data = json_data), create=True) as mocked_file: # Atidaromas failo testavimo failo srautas su duomenų nuskaitymų
            customer = Customer.from_json("tmp/c1.json.json")
        
        # Tikrinami ar duomenis buvo teisingai nuskaityti
        self.assertEqual(customer.get_name, "Jonas Jonaitis")
        self.assertEqual(customer.get_identifier(), 1)
        self.assertEqual(len(customer.shopping_cart), 2)

    def test_from_json_file_not_found(self): # Tikrinama ar failo neradus, išmetama klaida
        with patch('builtins.open', side_effect=FileNotFoundError):
            customer = Customer.from_json("non_existent.json")
            self.assertIsNone(customer)

if __name__ == '__main__':
    unittest.main()
