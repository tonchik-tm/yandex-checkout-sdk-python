# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.models.receipt import Receipt
from yandex_checkout.domain.request.capture_payment_request import CapturePaymentRequest


class TestCapturePaymentRequest(unittest.TestCase):
    def test_capture_request_cast(self):
        request = CapturePaymentRequest()
        request.receipt = Receipt({'phone': '79990000000', 'email': 'test@email.com', 'tax_system_code': 1, 'items': [
            {
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            }
        ]})
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})

        self.assertEqual(
            {
                'amount': {'value': 0.1, 'currency': Currency.RUB},
                'receipt': {
                    'customer': {'email': 'test@email.com', 'phone': '79990000000'},
                    'phone': '79990000000',
                    'email': 'test@email.com',
                    'items': [
                        {
                            "description": "Product 1",
                            "quantity": 2.0,
                            "amount": {
                                "value": 250.0,
                                "currency": Currency.RUB
                            },
                            "vat_code": 2
                        },
                        {
                            "description": "Product 2",
                            "quantity": 1.0,
                            "amount": {
                                "value": 100.0,
                                "currency": Currency.RUB
                            },
                            "vat_code": 2
                        }
                    ],
                    'tax_system_code': 1,
                }
            }, dict(request)
        )

    def test_capture_request_setters(self):
        request = CapturePaymentRequest({
            'receipt': {'phone': '79990000000', 'email': 'test@email.com', 'tax_system_code': 1, 'items': [
                {
                    "description": "Product 1",
                    "quantity": 2.0,
                    "amount": {
                        "value": 250.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2
                },
                {
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": {
                        "value": 100.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2
                }
            ]},
            'amount': {'value': 0.1, 'currency': Currency.RUB}
        })

        self.assertIsInstance(request.amount, Amount)
        self.assertIsInstance(request.receipt, Receipt)
        self.assertEqual(request.receipt.email, 'test@email.com')
        self.assertEqual(request.amount.currency, Currency.RUB)

        with self.assertRaises(TypeError):
            request.receipt = 'invalid receipt'

        with self.assertRaises(TypeError):
            request.amount = 'invalid amount'

    def test_capture_request_validate(self):
        request = CapturePaymentRequest()
        request.amount = {'value': 0.0, 'currency': Currency.RUB}
        with self.assertRaises(ValueError):
            request.validate()

        request = CapturePaymentRequest()
        request.amount = {'value': 0.1, 'currency': Currency.RUB}
        request.receipt = {'tax_system_code': 1, 'items': [
            {
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            }
        ]}

        with self.assertRaises(ValueError):
            request.validate()

        request = CapturePaymentRequest()
        request.amount = {'value': 0.1, 'currency': Currency.RUB}
        request.receipt = {'phone': '79990000000', 'items': [
            {
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
            }
        ]}

        with self.assertRaises(ValueError):
            request.validate()
