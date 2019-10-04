# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.common.confirmation_type import ConfirmationType
from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.request.payment_request_builder import PaymentRequestBuilder


class TestPaymentRequestBuilder(unittest.TestCase):
    def test_build_object(self):
        self.maxDiff = None
        builder = PaymentRequestBuilder()
        builder.set_receipt(
                {'phone': '79990000000', 'email': 'test@email.com', 'tax_system_code': 1, 'items': [
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
            ) \
            .set_amount({'value': 0.1, 'currency': Currency.RUB}) \
            .set_recipient({'account_id': '213', 'gateway_id': '123'}) \
            .set_capture(False) \
            .set_save_payment_method(True) \
            .set_confirmation({'type': ConfirmationType.REDIRECT, 'return_url': 'return.url'}) \
            .set_payment_method_data({'type': PaymentMethodType.WEBMONEY}) \
            .set_client_ip('192.0.0.0') \
            .set_payment_method_id('123') \
            .set_payment_token('99091209012') \
            .set_metadata({'key': 'value'})

        request = builder.build()

        self.assertEqual({
            'amount': {'value': 0.1, 'currency': Currency.RUB},
            'recipient': {
                'account_id': '213',
                'gateway_id': '123'
            },
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
            'confirmation': {'type': ConfirmationType.REDIRECT, 'return_url': 'return.url'},
            'client_ip': '192.0.0.0',
            'metadata': {'key': 'value'}
        }, dict(request))
