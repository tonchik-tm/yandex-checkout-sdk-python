# -*- coding: utf-8 -*-
import uuid

from yandex_checkout import PaymentResponse, ReceiptResponse
from yandex_checkout.client import ApiClient
from yandex_checkout.domain.common.http_verb import HttpVerb
from yandex_checkout.domain.request.receipt_request import ReceiptRequest
from yandex_checkout.domain.response.receipt_list_response import ReceiptListResponse


class Receipt:
    base_path = '/receipts'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def list(cls, params):
        if ('payment_id' in params or 'refund_id' in params) is False:
            raise TypeError('Invalid params value')

        instance = cls()
        path = cls.base_path

        response = instance.client.request(HttpVerb.GET, path, params)
        return ReceiptListResponse(response)

    @classmethod
    def create(cls, params, idempotency_key=None):
        """
        Create receipt

        :param params: data passed to API
        :param idempotency_key:
        :return: ReceiptResponse
        """
        instance = cls()
        path = cls.base_path

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = ReceiptRequest(params)
        elif isinstance(params, ReceiptRequest):
            params_object = params
        else:
            raise TypeError('Invalid params value type')

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return ReceiptResponse(response)
