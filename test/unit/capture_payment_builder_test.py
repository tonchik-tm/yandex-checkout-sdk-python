import unittest

from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.request.capture_payment_builder import CapturePaymentBuilder
from yandex_checkout.domain.request.capture_payment_request import CapturePaymentRequest


class CapturePaymentBuilderTest(unittest.TestCase):
    def test_build_object(self):
        builder = CapturePaymentBuilder()
        builder \
            .set_amount({'value': 0.1, 'currency': Currency.RUB}) \
            .set_receipt({'phone': '79990000000', 'email': 'test@email', 'tax_system_code': 1, 'items': [
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

        request = builder.build()

        self.assertIsInstance(request, CapturePaymentRequest)
        self.assertEqual(
            {
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
