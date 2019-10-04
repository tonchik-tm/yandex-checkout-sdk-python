# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.payment_data.card_type import CardType
from yandex_checkout.domain.models.payment_data.response.credit_card import CreditCard as ResponseCreditCard
from yandex_checkout.domain.models.payment_data.request.credit_card import CreditCard as RequestCreditCard


class TestCreditCard(unittest.TestCase):
    def test_credit_card_valid_params(self):
        credit_card = RequestCreditCard()
        credit_card.number = '8888888888880000'
        credit_card.expiry_year = '2018'
        credit_card.expiry_month = '10'
        credit_card.csc = '111'
        credit_card.cardholder = 'test'

        self.assertEqual({
            'number': '8888888888880000',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }, dict(credit_card))

        credit_card = ResponseCreditCard()
        credit_card.last4 = '0000'
        credit_card.expiry_year = '2010'
        credit_card.expiry_month = '02'
        credit_card.card_type = CardType.VISA

        self.assertEqual({
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }, dict(credit_card))

    def test_credit_card_invalid_params(self):
        credit_card = RequestCreditCard()

        with self.assertRaises(ValueError):
            credit_card.number = 'invalid number'

        with self.assertRaises(ValueError):
            credit_card.expiry_year = 'invalid expiry_year'

        with self.assertRaises(ValueError):
            credit_card.expiry_month = 'invalid expiry_month'

        with self.assertRaises(ValueError):
            credit_card.csc = 'invalid csc'

        with self.assertRaises(ValueError):
            credit_card.cardholder = '123'

        credit_card = ResponseCreditCard()

        with self.assertRaises(ValueError):
            credit_card.last4 = '00001'

        with self.assertRaises(ValueError):
            credit_card.expiry_year = 'invalid expiry_year'

        with self.assertRaises(ValueError):
            credit_card.expiry_month = 'invalid expiry_month'

        with self.assertRaises(ValueError):
            credit_card.card_type = 'invalid card_type'
