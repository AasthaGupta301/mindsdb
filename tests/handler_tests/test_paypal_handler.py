import os
import unittest

from mindsdb.integrations.handlers.paypal_handler.paypal_handler import PayPalHandler
from mindsdb.api.mysql.mysql_proxy.libs.constants.response_type import RESPONSE_TYPE


class PayPalHandlerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs = {
            "connection_data": {
                "mode": os.environ.get('MODE'),
                "client_id": os.environ.get('CLIENT_ID'),
                "client_secret": os.environ.get('CLIENT_SECRET'),
            }
        }
        cls.handler = PayPalHandler('test_paypal_handler', **cls.kwargs)

    def test_0_check_connection(self):
        assert self.handler.check_connection()

    def test_1_get_tables(self):
        tables = self.handler.get_tables()
        assert tables.type is not RESPONSE_TYPE.ERROR

    def test_2_select_payments_query(self):
        query = "SELECT * FROM test_paypal_handler.payments"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

    def test_3_select_invoices_query(self):
        query = "SELECT * FROM test_paypal_handler.invoices"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

    def test_4_select_subscriptions_query(self):
        query = "SELECT * FROM test_paypal_handler.subscriptions"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

    def test_5_select_orders_query(self):
        query = "SELECT * FROM test_paypal_handler.orders WHERE ids = ('')"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

