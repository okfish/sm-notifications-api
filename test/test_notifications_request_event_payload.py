# coding: utf-8


import unittest

from sm_notifications_api.models.notifications_request_event_payload import NotificationsRequestEventPayload

class TestNotificationsRequestEventPayload(unittest.TestCase):
    """NotificationsRequestEventPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationsRequestEventPayload:
        """Test NotificationsRequestEventPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationsRequestEventPayload`
        """
        model = NotificationsRequestEventPayload()
        if include_optional:
            return NotificationsRequestEventPayload(
                order_id = 'metro:order_uuid',
                order_uuid = '265cb601-a78a-4862-9e9d-d6b48d6a0a3f',
                code = '1234',
                handout_code = '1234',
                estimated_assembly_at = '2021-12-20T14:00:00+03:00',
                number = '1234',
                order = sm_notifications_api.models.основные_поля_события.Основные поля события(
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
                        ], )
            )
        else:
            return NotificationsRequestEventPayload(
                order_id = 'metro:order_uuid',
                order_uuid = '265cb601-a78a-4862-9e9d-d6b48d6a0a3f',
        )
        """

    def testNotificationsRequestEventPayload(self):
        """Test NotificationsRequestEventPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
