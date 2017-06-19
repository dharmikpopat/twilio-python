import unittest
import six

from tests.holodeck import Holodeck
from twilio.rest import Client
from twilio.http.response import Response


class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.account_sid = 'AC' + 'a' * 32
        self.auth_token = 'AUTHTOKEN'
        self.holodeck = Holodeck()
        self.client = Client(username=self.account_sid,
                             password=self.auth_token,
                             http_client=self.holodeck)


class MockResponse(Response):
    def __init__(self, status, content):
        # Here we will convert content (a string type) to a bytes object in
        # Python 3 for consistency purposes
        if (six.PY3):
            content = bytes(content, 'utf-8')
        super(MockResponse, self).__init__(status, content)
