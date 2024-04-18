import unittest
from shop.shop_customers import Customer

class TestCustomer(unittest.TestCase):
    def test_name_privacy(self): # Tikrinamas ar kliento vardas yra privatus, bandant tiesiogiai jį išspaudinti
        customer = Customer("Jonas Jonaitis")
        with self.assertRaises(AttributeError):
            print(customer.__name)

    def test_name_empty(self): # Tikrinama ar neleidžiama sukurti naują klienta su tuščių vardu
        with self.assertRaises(TypeError):
            Customer("")

    def test_name_instance(self): # Tikrinama ar neleidžiama sukurti naują klienta su netinkamu vardu
        with self.assertRaises(TypeError):
            Customer(0)

    def test_indentifier(self): # Tikrinama ar pasikeičia identifikatorius, pridėjus naują klientą
        oldIdentifier = Customer.identifier
        customer = Customer("Jonas Jonaitis")

        self.assertEqual(oldIdentifier + 1, customer.get_identifier())

    def test_full_info(self): # Tikrinama ar full_info gražina tinkamą informaciją
        customer_name = "Jonas Jonaitis"
        customer = Customer(customer_name)
        self.assertEqual("Vardas: " + customer_name+ " | " + str(customer.get_identifier()), customer.full_info())

    