# coding: utf-8


import unittest

from sm_notifications_api.models.order_event_positions_inner_marking_code_inner import OrderEventPositionsInnerMarkingCodeInner

class TestOrderEventPositionsInnerMarkingCodeInner(unittest.TestCase):
    """OrderEventPositionsInnerMarkingCodeInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderEventPositionsInnerMarkingCodeInner:
        """Test OrderEventPositionsInnerMarkingCodeInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderEventPositionsInnerMarkingCodeInner`
        """
        model = OrderEventPositionsInnerMarkingCodeInner()
        if include_optional:
            return OrderEventPositionsInnerMarkingCodeInner(
                value = '1111111'
            )
        else:
            return OrderEventPositionsInnerMarkingCodeInner(
        )
        """

    def testOrderEventPositionsInnerMarkingCodeInner(self):
        """Test OrderEventPositionsInnerMarkingCodeInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
