# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.receipt_item import PaymentMode, PaymentSubject
from yandex_checkout.domain.response.receipt_response import ReceiptResponse


class TestReceiptResponse(unittest.TestCase):
    def test_response_cast(self):
        response = ReceiptResponse({
            "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
            "type": "payment",
            "payment_id": "215d8da0-000f-50be-b000-0003308c89be",
            "status": "succeeded",
            "fiscal_document_number": "3986",
            "fiscal_storage_number": "9288000100115785",
            "fiscal_attribute": "2617603921",
            "registered_at": "2019-05-13T17:56:00.000+03:00",
            "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
            "tax_system_code": 1,
            "items": [{
                "description": "Capybara",
                "quantity": 5,
                "amount": {
                    "value": "2500.50",
                    "currency": "RUB"
                },
                "vat_code": 2,
                "payment_mode": PaymentMode.FULL_PAYMENT,
                "payment_subject": PaymentSubject.COMMODITY
            }]
        })

        self.assertIsInstance(response.items, list)

        self.assertEqual(response.id, 'rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9')
        self.assertEqual(response.type, 'payment')
        self.assertEqual(response.payment_id, '215d8da0-000f-50be-b000-0003308c89be')
        self.assertEqual(response.status, 'succeeded')
        self.assertEqual(response.receipt_registration, 'succeeded')
        self.assertEqual(response.fiscal_document_number, '3986')
        self.assertEqual(response.fiscal_storage_number, '9288000100115785')
        self.assertEqual(response.fiscal_attribute, '2617603921')
        self.assertEqual(response.registered_at, '2019-05-13T17:56:00.000+03:00')
        self.assertEqual(response.tax_system_code, 1)
        self.assertEqual(response.fiscal_provider_id, 'fd9e9404-eaca-4000-8ec9-dc228ead2345')

        self.assertEqual(response.items[0].description, 'Capybara')
        self.assertEqual(response.items[0].quantity, 5.0)
        self.assertEqual(response.items[0].amount.value, 2500.50)
        self.assertEqual(response.items[0].amount.currency, 'RUB')
        self.assertEqual(response.items[0].vat_code, 2)
        self.assertEqual(response.items[0].payment_mode, PaymentMode.FULL_PAYMENT)
        self.assertEqual(response.items[0].payment_subject, PaymentSubject.COMMODITY)