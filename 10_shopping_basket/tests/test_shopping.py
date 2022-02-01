import unittest
from shopping.basket import ShoppingBasket

class TestShoppingBasketWithNoProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket without any products...')
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        pass

    def test_getting_product_out_or_range_should_raise_error(self):
        pass

    def test_total_amount_should_be_zero(self):
        pass

class TestShoppingBasketWithOneProduct():
    pass

