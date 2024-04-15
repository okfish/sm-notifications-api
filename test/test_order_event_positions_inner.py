# coding: utf-8


import unittest

from sm_notifications_api.models.order_event_positions_inner import OrderEventPositionsInner

class TestOrderEventPositionsInner(unittest.TestCase):
    """OrderEventPositionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderEventPositionsInner:
        """Test OrderEventPositionsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderEventPositionsInner`
        """
        model = OrderEventPositionsInner()
        if include_optional:
            return OrderEventPositionsInner(
                id = '123456',
                quantity = 1.0,
                weight = '1000',
                marking_code = [
                    sm_notifications_api.models.маркировка.Маркировка(
                        value = '1111111', )
                    ],
                replaced_by_id = '789012'
            )
        else:
            return OrderEventPositionsInner(
                id = '123456',
                quantity = 1.0,
        )
        """

    def testOrderEventPositionsInner(self):
        """Test OrderEventPositionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
