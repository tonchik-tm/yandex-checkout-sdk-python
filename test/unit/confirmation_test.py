import unittest

from yandex_checkout.domain.common.confirmation_type import ConfirmationType
from yandex_checkout.domain.models.confirmation.request.confirmation_redirect import \
    ConfirmationRedirect as RequestConfirmationRedirect
from yandex_checkout.domain.models.confirmation.response.confirmation_redirect import \
    ConfirmationRedirect as ResponseConfirmationRedirect


class ConfirmationTest(unittest.TestCase):
    def test_confirmation_request(self):
        confirmation = RequestConfirmationRedirect()
        confirmation.type = ConfirmationType.REDIRECT
        confirmation.enforce = True
        confirmation.return_url = 'return.url'

        self.assertEqual(confirmation.type, ConfirmationType.REDIRECT)
        self.assertTrue(confirmation.enforce)
        self.assertEqual(
            {'type': ConfirmationType.REDIRECT, 'enforce': True, 'return_url': 'return.url'},
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''

    def test_confirmation_response(self):
        confirmation = ResponseConfirmationRedirect()
        confirmation.type = ConfirmationType.REDIRECT
        confirmation.enforce = True
        confirmation.return_url = 'return.url'
        confirmation.confirmation_url = 'confirmation.url'
        self.assertEqual(confirmation.type, ConfirmationType.REDIRECT)
        self.assertTrue(confirmation.enforce)
        self.assertEqual(
            {
                'type': ConfirmationType.REDIRECT,
                'enforce': True,
                'return_url': 'return.url',
                'confirmation_url': 'confirmation.url'
            },
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''
