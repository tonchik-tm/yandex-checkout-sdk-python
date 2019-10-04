# -*- coding: utf-8 -*-
import unittest

from yandex_checkout import Currency, ReceiptItem
from yandex_checkout.domain.common.receipt_type import ReceiptType
from yandex_checkout.domain.models.receipt_customer import ReceiptCustomer
from yandex_checkout.domain.models.settlement import SettlementType, Settlement
from yandex_checkout.domain.request.receipt_request import ReceiptRequest


class TestReceiptRequest(unittest.TestCase):
    def test_request_cast(self):
        request = ReceiptRequest()
        request.type = ReceiptType.PAYMENT
        request.send = True
        request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})
        request.items = [
            ReceiptItem({
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            }),
            ReceiptItem({
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            })
        ]
        request.settlements = [
            Settlement({
                'type': SettlementType.CASHLESS,
                'amount': {
                    'value': 250.0,
                    'currency': Currency.RUB
                }
            })
        ]
        request.tax_system_code = 1
        request.payment_id = '215d8da0-000f-50be-b000-0003308c89be'

        self.assertEqual({
            'type': ReceiptType.PAYMENT,
            'send': True,
            'customer': {'email': 'test@email.com', 'phone': '79990000000'},
            'items': [
                {
                    'description': 'Product 1',
                    'quantity': 2.0,
                    'amount': {
                        'value': 250.0,
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                },
                {
                    'description': 'Product 2',
                    'quantity': 1.0,
                    'amount': {
                        'value': 100.0,
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                }
            ],
            'settlements': [
                {
                    'type': SettlementType.CASHLESS,
                    'amount': {
                        'value': 250.0,
                        'currency': Currency.RUB
                    }
                }
            ],
            'tax_system_code': 1,
            'payment_id': '215d8da0-000f-50be-b000-0003308c89be'
        }, dict(request))

    def test_request_setters(self):
        request = ReceiptRequest({
            'type': ReceiptType.PAYMENT,
            'send': True,
            'customer': {'email': 'test@email.com', 'phone': '79990000000'},
            'items': [
                {
                    'description': 'Product 1',
                    'quantity': 2.0,
                    'amount': {
                        'value': 250.0,
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                },
                {
                    'description': 'Product 2',
                    'quantity': 1.0,
                    'amount': {
                        'value': 100.0,
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                }
            ],
            'settlements': [
                {
                    'type': SettlementType.CASHLESS,
                    'amount': {
                        'value': 250.0,
                        'currency': Currency.RUB
                    }
                }
            ],
            'tax_system_code': 1,
            'payment_id': '215d8da0-000f-50be-b000-0003308c89be'
        })

        self.assertIsInstance(request.customer, ReceiptCustomer)
        self.assertIsInstance(request.items, list)
        self.assertIsInstance(request.settlements, list)

        with self.assertRaises(TypeError):
            request.customer = 'invalid customer'

        with self.assertRaises(TypeError):
            request.items = 'invalid items'

        with self.assertRaises(TypeError):
            request.settlements = 'invalid settlements'

    def test_request_validate(self):
        request = ReceiptRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.type = ReceiptType.PAYMENT

        with self.assertRaises(ValueError):
            request.validate()

        request.send = True

        with self.assertRaises(ValueError):
            request.validate()

        request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})

        with self.assertRaises(ValueError):
            request.validate()

        request.items = [
            ReceiptItem({
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            }),
            ReceiptItem({
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            })
        ]

        with self.assertRaises(ValueError):
            request.validate()

        request.settlements = [
            Settlement({
                'type': SettlementType.CASHLESS,
                'amount': {
                    'value': 250.0,
                    'currency': Currency.RUB
                }
            })
        ]

        with self.assertRaises(ValueError):
            request.validate()

        request.tax_system_code = 1

        with self.assertRaises(ValueError):
            request.validate()

        request.refund_id = '215d8da0-000f-50be-b000-0003308c89be'

        with self.assertRaises(ValueError):
            request.validate()

        request.payment_id = '215d8da0-000f-50be-b000-0003308c89be'

        self.assertIsNone(request.validate())
