

import unittest
from random import randint, sample, uniform
from acme import Product
from acme_report import generate_products, adj_list, noun_list


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_explode(self):
        """Test stealability and explode methods."""
        prod = Product(name='Test Product', price=10,
                       weight=20, flammability=0.5)
        self.assertEqual(prod.stealability(), "Kinda stealable")
        self.assertEqual(prod.explode(), "boom")


class AcmeReportTests(unittest.TestCase):
    """Test report methods."""

    def test_default_num_products(self):
        """Test default number of products being 30."""
        num_prods = generate_products()
        self.assertEqual(len(num_prods), 30)

    def test_legal_names(self):
        """Test validity of generated names."""
        name_prods = generate_products()
        for x in name_prods:
            adj = sample(adj_list, 1)[0]
            noun = sample(noun_list, 1)[0]
            name = adj + ' ' + noun
            self.assertIn(name, name)


if __name__ == '__main__':
    unittest.main()
