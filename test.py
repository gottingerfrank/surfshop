#!/usr/bin/env python3


# Write your code below:
import surfshop
import unittest
import datetime


class SurfShopTests(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboards(self):
        for i in range(1, 5):
            num_boards = self.cart.add_surfboards(i)
            if i == 1:
                self.assertEqual(num_boards, f"Successfully added {i} surfboard to cart!")
            else:
                self.assertEqual(num_boards, f"Successfully added {i} surfboards to cart!")
            self.cart = surfshop.ShoppingCart()

    # def test_add_surfboards(self):
    #     self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')
    #     self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')

    @unittest.skip
    def test_add_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    def test_set_checkout_date(self):
        test_date = datetime.datetime(2021, 1, 1)
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, test_date)

    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)


# run tests
unittest.main()
