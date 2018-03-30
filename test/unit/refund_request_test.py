import unittest

from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.models.receipt import Receipt
from yandex_checkout.domain.request.refund_request import RefundRequest


class RefundRequestTest(unittest.TestCase):
    def test_refund_cast(self):
        self.maxDiff = None
        request = RefundRequest()
        request.payment_id = '21a632d2-000f-5061-a000-01e90bc2de12'
        request.description = 'test comment'
        request.receipt = Receipt({'phone': '79990000000', 'email': 'test@email', 'tax_system_code': 1, 'items': [
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

        self.assertEqual({
            'payment_id': '21a632d2-000f-5061-a000-01e90bc2de12',
            'description': 'test comment',
            'receipt': {'phone': '79990000000', 'email': 'test@email', 'tax_system_code': 1, 'items': [
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
        }, dict(request))

    def test_request_setters(self):
        request = RefundRequest({
            'payment_id': '21a632d2-000f-5061-a000-01e90bc2de12',
            'description': 'test comment',
            'receipt': {'phone': '79990000000', 'email': 'test@email', 'tax_system_code': 1, 'items': [
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

        self.assertIsInstance(request.receipt, Receipt)
        self.assertIsInstance(request.amount, Amount)

    def test_invalid_values(self):
        request = RefundRequest()
        with self.assertRaises(TypeError):
            request.receipt = 'invalid receipt'

        with self.assertRaises(TypeError):
            request.amount = 'invalid amount'

        with self.assertRaises(ValueError):
            request.payment_id = 'invalid payment_id'

        with self.assertRaises(ValueError):
            request.description = ''

    def test_request_validate(self):
        request = RefundRequest()
        with self.assertRaises(ValueError):
            request.validate()

        request.payment_id = '21a632d2-000f-5061-a000-01e90bc2de12'
        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.0, 'currency': Currency.RUB})
        with self.assertRaises(ValueError):
            request.validate()

        request.amount.value = 0.1

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
