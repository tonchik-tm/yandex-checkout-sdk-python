# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.authorization_details import AuthorizationDetails
from yandex_checkout.domain.models.cancellation_details import CancellationDetails
from yandex_checkout.domain.models.confirmation.confirmation import Confirmation
from yandex_checkout.domain.models.payment_data.response.payment_data_bank_card import PaymentDataBankCard
from yandex_checkout.domain.models.recipient import Recipient
from yandex_checkout.domain.response.payment_response import PaymentResponse


class TestPaymentResponse(unittest.TestCase):
    def test_response_cast(self):
        response = PaymentResponse({
            "id": "21b23365-000f-500b-9000-070fa3554403",
            "amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://test.test/test",
                "confirmation_url": "https://url",
                "enforce": False
            },
            "payment_method": {
                "type": "bank_card",
                "id": "21b23365-000f-500b-9000-070fa3554403",
                "saved": False
            },
            "status": "pending",
            "recipient": {
                "account_id": "67192",
                "gateway_id": "352780"
            },
            "refunded_amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "receipt_registration": "pending",
            "created_at": "2017-11-30T15:11:33+00:00",
            "expires_at": "2017-11-30T15:11:33+00:00",
            "captured_at": "2017-11-30T15:11:33+00:00",
            "paid": False,
            "refundable": False,
            "test": False,
            "metadata": {
                "float_value": "123.32",
                "key": "data"
            },
            'cancellation_details': {
                'party': 'yandex_checkout',
                'reason': 'fraud_suspected'
            },
            'authorization_details': {
                'rrn': 'rrn',
                'auth_code': 'auth_code'
            }
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.recipient, Recipient)
        self.assertIsInstance(response.payment_method, PaymentDataBankCard)
        self.assertIsInstance(response.confirmation, Confirmation)
        self.assertIsInstance(response.cancellation_details, CancellationDetails)
        self.assertIsInstance(response.authorization_details, AuthorizationDetails)
        self.assertEqual(response.metadata, {
            "float_value": "123.32",
            "key": "data"
        })
        self.assertFalse(response.paid)
        self.assertFalse(response.refundable)
        self.assertFalse(response.test)
        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.status, "pending")
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.expires_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.captured_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, "pending")
        self.assertEqual(response.refunded_amount, {
            "value": "1000.00",
            "currency": "RUB"
        })
