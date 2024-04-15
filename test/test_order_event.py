# coding: utf-8


import unittest

from sm_notifications_api.models.order_event import OrderEvent

class TestOrderEvent(unittest.TestCase):
    """OrderEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderEvent:
        """Test OrderEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderEvent`
        """
        model = OrderEvent()
        if include_optional:
            return OrderEvent(
                original_order_id = 'order.created',
                positions = [
                    sm_notifications_api.models.позиция_заказа.Позиция заказа(
                        id = '123456',
                        quantity = 1.0,
                        weight = '1000',
                        marking_code = [
                            sm_notifications_api.models.маркировка.Маркировка(
                                value = '1111111', )
                            ],
                        replaced_by_id = '789012', )
                    ]
            )
        else:
            return OrderEvent(
                positions = [
                    sm_notifications_api.models.позиция_заказа.Позиция заказа(
                        id = '123456',
                        quantity = 1.0,
                        weight = '1000',
                        marking_code = [
                            sm_notifications_api.models.маркировка.Маркировка(
                                value = '1111111', )
                            ],
                        replaced_by_id = '789012', )
                    ],
        )
        """

    def testOrderEvent(self):
        """Test OrderEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
