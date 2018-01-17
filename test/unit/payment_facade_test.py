import unittest

from unittest.mock import patch
from yandex_checkout.configuration import Configuration
from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.payment_data.response.payment_data_bank_card import PaymentDataBankCard
from yandex_checkout.domain.request.capture_payment_request import CapturePaymentRequest
from yandex_checkout.domain.request.payment_request import PaymentRequest
from yandex_checkout.domain.response.payment_response import PaymentResponse
from yandex_checkout.payment import Payment

import yandex_checkout.client


class PaymentFacadeTest(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create_payment_with_dict(self):
        self.maxDiff = None
        payment_facade = Payment()
        with patch('yandex_checkout.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }
            payment = payment_facade.create({
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }, 'asd213')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_payment_with_object(self):
        self.maxDiff = None
        payment_facade = Payment()
        with patch('yandex_checkout.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }
            payment = payment_facade.create(PaymentRequest({
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }))

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_capture_with_dict(self):
        payment_facade = Payment()
        with patch('yandex_checkout.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }

            payment = payment_facade.capture('21b23b5b-000f-5061-a000-0674e49a8c10', {
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }, 'asd213')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_capture_with_object(self):
        payment_facade = Payment()
        with patch('yandex_checkout.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }

            payment = payment_facade.capture('21b23b5b-000f-5061-a000-0674e49a8c10', CapturePaymentRequest({
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }))

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_capture(self):
        payment_facade = Payment()
        with patch('yandex_checkout.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }

            payment = payment_facade.capture('21b23b5b-000f-5061-a000-0674e49a8c10')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_payment_info(self):
        payment_facade = Payment()
        with patch('yandex_checkout.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }
            payment = payment_facade.find_one('21b23b5b-000f-5061-a000-0674e49a8c10')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_payment_cancel(self):
        payment_facade = Payment()
        with patch('yandex_checkout.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'canceled'
            }
            payment = payment_facade.cancel('21b23b5b-000f-5061-a000-0674e49a8c10')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Payment().find_one('')

        with self.assertRaises(TypeError):
            Payment().create('invalid params')

        with self.assertRaises(ValueError):
            Payment().capture(111)

        with self.assertRaises(ValueError):
            Payment().cancel('')
