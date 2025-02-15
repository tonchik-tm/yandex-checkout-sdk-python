# -*- coding: utf-8 -*-

from yandex_checkout import ReceiptItem
from yandex_checkout.domain.common.receipt_type import ReceiptType
from yandex_checkout.domain.common.request_object import RequestObject
from yandex_checkout.domain.models.receipt_customer import ReceiptCustomer
from yandex_checkout.domain.models.settlement import Settlement


class ReceiptRequest(RequestObject):

    __type = None

    __send = None

    __customer = None

    __tax_system_code = None

    __items = None

    __settlements = None

    __payment_id = None

    __refund_id = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)

    @property
    def send(self):
        return self.__send

    @send.setter
    def send(self, value):
        if isinstance(value, bool):
            self.__send = value
        else:
            raise TypeError('Invalid send value type in receipt_request')

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, dict):
            self.__customer = ReceiptCustomer(value)
        elif isinstance(value, ReceiptCustomer):
            self.__customer = value
        else:
            raise TypeError('Invalid customer value type in receipt_request')

    @property
    def tax_system_code(self):
        return self.__tax_system_code

    @tax_system_code.setter
    def tax_system_code(self, value):
        if isinstance(value, int):
            self.__tax_system_code = value
        else:
            raise TypeError('Invalid tax_system_code value type in receipt_request')

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    items.append(ReceiptItem(item))
                elif isinstance(item, ReceiptItem):
                    items.append(item)
                else:
                    raise TypeError('Invalid item type in receipt.items')

            self.__items = items
        else:
            raise TypeError('Invalid items value type in receipt_request')

    @property
    def settlements(self):
        return self.__settlements

    @settlements.setter
    def settlements(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    items.append(Settlement(item))
                elif isinstance(item, Settlement):
                    items.append(item)
                else:
                    raise TypeError('Invalid settlement type in receipt.settlements')

            self.__settlements = items
        else:
            raise TypeError('Invalid settlements value type in receipt_request')

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__refund_id = None
        self.__payment_id = str(value)

    @property
    def refund_id(self):
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__payment_id = None
        self.__refund_id = str(value)

    def validate(self):
        if self.type is None:
            self.__set_validation_error('Receipt type not specified')

        if self.send is None:
            self.__set_validation_error('Receipt send not specified')

        if self.customer is not None:
            email = self.customer.email
            phone = self.customer.phone
            if not email and not phone:
                self.__set_validation_error('Both email and phone values are empty in customer')
        else:
            self.__set_validation_error('Receipt customer not specified')

        if not self.has_items():
            self.__set_validation_error('Receipt items not specified')

        if not self.has_settlements():
            self.__set_validation_error('Receipt settlements not specified')

        if self.type is ReceiptType.PAYMENT and self.payment_id is None:
            self.__set_validation_error('Receipt payment_id not specified')

        if self.type is ReceiptType.REFUND and self.refund_id is None:
            self.__set_validation_error('Receipt refund_id not specified')

    def has_items(self):
        return bool(self.items)

    def has_settlements(self):
        return bool(self.settlements)

    def __set_validation_error(self, message):
        raise ValueError(message)
