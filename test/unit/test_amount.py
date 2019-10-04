# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.currency import Currency


class TestAmount(unittest.TestCase):
    def test_amount_cast(self):
        amount = Amount()
        amount.value = 0.1
        amount.currency = Currency.RUB

        self.assertEqual({'value': 0.1, 'currency': Currency.RUB}, dict(amount))
