# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.common.confirmation_type import ConfirmationType
from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.confirmation.confirmation import Confirmation
from yandex_checkout.domain.models.confirmation.request.confirmation_redirect import ConfirmationRedirect
from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.models.payment_data.payment_data import PaymentData
from yandex_checkout.domain.models.payment_data.request.payment_data_webmoney import PaymentDataWebmoney
from yandex_checkout.domain.models.receipt import Receipt
from yandex_checkout.domain.models.recipient import Recipient
from yandex_checkout.domain.request.payment_request import PaymentRequest


class TestPaymentRequest(unittest.TestCase):
    def test_request_cast(self):
        self.maxDiff = None
        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.description = 'Test description'
        request.recipient = Recipient({
            'account_id': '213',
            'gateway_id': '123'
        })
        request.save_payment_method = True
        request.capture = False
        request.payment_method_data = PaymentDataWebmoney()
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
        request.payment_method_id = '123'
        request.payment_token = '99091209012'
        request.confirmation = ConfirmationRedirect({'locale': 'ru_RU', 'return_url': 'return.url'})
        request.client_ip = '192.0.0.0'
        request.metadata = {'key': 'value'}

        self.assertEqual({
            'amount': {'value': 0.1, 'currency': Currency.RUB},
            'recipient': {
                'account_id': '213',
                'gateway_id': '123'
            },
            'description': 'Test description',
            'save_payment_method': True,
            'capture': False,
            'payment_method_data': {'type': PaymentMethodType.WEBMONEY},
            'receipt': {
                'customer': {'email': 'test@email.com', 'phone': '79990000000'},
                'phone': '79990000000',
                'email': 'test@email.com',
                'tax_system_code': 1,
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
                ]},
            'payment_method_id': '123',
            'payment_token': '99091209012',
            'confirmation': {'type': ConfirmationType.REDIRECT, 'locale': 'ru_RU', 'return_url': 'return.url'},
            'client_ip': '192.0.0.0',
            'metadata': {'key': 'value'}
        }, dict(request))

    def test_request_setters(self):
        request = PaymentRequest({
            'amount': {'value': 0.1, 'currency': Currency.RUB},
            'recipient': {
                'account_id': '213',
                'gateway_id': '123'
            },
            'save_payment_method': True,
            'capture': False,
            'payment_method_data': {'type': PaymentMethodType.WEBMONEY},
            'receipt': {
                'phone': '79990000000',
                'email': 'test@email.com',
                'tax_system_code': 1,
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
                ]},
            'payment_method_id': '123',
            'payment_token': '99091209012',
            'confirmation': {'type': ConfirmationType.REDIRECT, 'return_url': 'return.url'},
            'client_ip': '192.0.0.0',
            'metadata': {'key': 'value'}
        })

        self.assertIsInstance(request.confirmation, Confirmation)
        self.assertIsInstance(request.amount, Amount)
        self.assertIsInstance(request.receipt, Receipt)
        self.assertIsInstance(request.recipient, Recipient)
        self.assertIsInstance(request.payment_method_data, PaymentData)

        with self.assertRaises(TypeError):
            request.receipt = 'invalid receipt'

        with self.assertRaises(TypeError):
            request.amount = 'invalid amount'

        with self.assertRaises(TypeError):
            request.recipient = 'invalid recipient'

        with self.assertRaises(TypeError):
            request.confirmation = 'invalid confirmation'

        with self.assertRaises(TypeError):
            request.payment_method_data = 'invalid payment_method_data'

        with self.assertRaises(ValueError):
            request.payment_token = ''

    def test_request_validate(self):
        request = PaymentRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.0, 'currency': Currency.RUB})

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
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

        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_token = '123'
        request.payment_method_id = '123'
        with self.assertRaises(ValueError):
            request.validate()

        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_token = '123'
        request.payment_method_data = PaymentDataWebmoney()
        with self.assertRaises(ValueError):
            request.validate()

        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_method_id = '123'
        request.payment_method_data = PaymentDataWebmoney()
        with self.assertRaises(ValueError):
            request.validate()
