# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.response_object import ResponseObject
from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.authorization_details import AuthorizationDetails
from yandex_checkout.domain.models.cancellation_details import CancellationDetails
from yandex_checkout.domain.models.confirmation.confirmation_factory import ConfirmationFactory
from yandex_checkout.domain.models.payment_data.payment_data_factory import PaymentDataFactory
from yandex_checkout.domain.models.recipient import Recipient


class PaymentResponse(ResponseObject):
    """
    Class representing response object.

    Contains data
    """
    __id = None

    __status = None

    __recipient = None

    __amount = None

    __description = None

    __payment_method = None

    __created_at = None

    __captured_at = None

    __confirmation = None

    __test = None

    __refunded_amount = None

    __paid = None

    __refundable = None

    __receipt_registration = None

    __metadata = None

    __expires_at = None

    __cancellation_details = None

    __authorization_details = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def recipient(self):
        return self.__recipient

    @recipient.setter
    def recipient(self, value):
        self.__recipient = Recipient(value)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = Amount(value)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = PaymentDataFactory().create(value, self.context())

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def captured_at(self):
        return self.__captured_at

    @captured_at.setter
    def captured_at(self, value):
        self.__captured_at = value

    @property
    def confirmation(self):
        return self.__confirmation

    @confirmation.setter
    def confirmation(self, value):
        self.__confirmation = ConfirmationFactory().create(value, self.context())

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, value):
        self.__test = bool(value)

    @property
    def refunded_amount(self):
        return self.__refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, value):
        self.__refunded_amount = value

    @property
    def paid(self):
        return self.__paid

    @paid.setter
    def paid(self, value):
        self.__paid = bool(value)

    @property
    def refundable(self):
        return self.__refundable

    @refundable.setter
    def refundable(self, value):
        self.__refundable = bool(value)

    @property
    def receipt_registration(self):
        return self.__receipt_registration

    @receipt_registration.setter
    def receipt_registration(self, value):
        self.__receipt_registration = value

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value

    @property
    def expires_at(self):
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value

    @property
    def cancellation_details(self):
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = CancellationDetails(value)

    @property
    def authorization_details(self):
        return self.__authorization_details

    @authorization_details.setter
    def authorization_details(self, value):
        self.__authorization_details = AuthorizationDetails(value)
