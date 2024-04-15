# coding: utf-8
import asyncio
import unittest
from dotenv import dotenv_values

import sm_notifications_api as smn


config = smn.configuration.Configuration(host='https://integrations-gw.sbermarket.ru/chapi')

credentials = dotenv_values("../.env.test")

config.api_key['client_token_auth'] = credentials['CLIENT_TOKEN']
config.api_key_prefix['client_token_auth'] = ''
config.retries = 3  # this enables aiohttp_retry client

WRONG_ID = 'H1231231123'
ORDER_ID = 'HTcc1e73ac-e48d-4629-82d6-d1b10d36de96'
WRONG_TOKEN = 'GciOiJSUzI1NiIsInR5cCIgOiAi'


class TestNotificationsApi(unittest.IsolatedAsyncioTestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self) -> None:
        self.client = smn.ApiClient(config)
        self.api = smn.NotificationsApi(api_client=self.client)

    async def asyncTearDown(self) -> None:
        await self.client.close()

    async def test_notifications_wrong_creds(self) -> None:
        """Test case for notifications

        Отправка события
        """
        self.client.configuration.api_key['client_token_auth'] = WRONG_TOKEN
        order_accepted = smn.NotificationsRequestEvent(type='order.accepted',
                                                       payload=smn.NotificationsRequestEventPayload(order_id=WRONG_ID,
                                                                                                    ))
        req = smn.models.NotificationsRequest(event=order_accepted)
        print(req)

        api_response = None

        try:
            # send notification
            api_response = await self.api.notifications(notifications_request=req, api_version='3.0')
        except smn.ApiException as e:
            print(f"Exception when calling {self.api.__class__.__name__} : {e}")

            # self.assertIsInstance(api_response, smn.api_response.ApiResponse)
            self.assertEqual(e.status, 404)

        if api_response is not None:
            print(api_response.to_str())


    async def test_notifications_wrong_order(self) -> None:
        """Test case for notifications

        Отправка события
        """
        order_accepted = smn.NotificationsRequestEvent(type='order.accepted',
                                                       payload=smn.NotificationsRequestEventPayload(order_id=WRONG_ID,
                                                                                                    ))
        req = smn.models.NotificationsRequest(event=order_accepted)
        print(req)

        api_response = None

        try:
            # send notification
            api_response = await self.api.notifications(notifications_request=req, api_version='3.0')
        except smn.ApiException as e:
            print(f"Exception when calling {self.api.__class__.__name__} : {e}")

            # self.assertIsInstance(api_response, smn.models.ErrorsObject)
            self.assertEqual(e.status, 422)

        if api_response is not None:
            print(api_response.to_str())

    async def test_notifications(self) -> None:
        """Test case for notifications

        Отправка события
        """

        api_response = None

        try:
            # send notification
            _type = 'order.accepted'
            _event = smn.NotificationsRequestEvent(type=_type,
                                                   payload=smn.NotificationsRequestEventPayload(order_id=ORDER_ID,
                                                                                                ))
            req = smn.models.NotificationsRequest(event=_event)
            api_response = await self.api.notifications(notifications_request=req, api_version='3.0')
            print(req)
            print('Sleep for 5s...')
            await asyncio.sleep(5)

            _type = 'order.in_work'
            _event = smn.NotificationsRequestEvent(type=_type,
                                                   payload=smn.NotificationsRequestEventPayload(order_id=ORDER_ID,
                                                                                                ))
            req = smn.models.NotificationsRequest(event=_event)
            api_response = await self.api.notifications(notifications_request=req, api_version='3.0')
            print(req)
            print('Sleep for 5s...')
            await asyncio.sleep(5)

            _type = 'order.ready_for_delivery'
            _event = smn.NotificationsRequestEvent(
                type=_type,
                payload=smn.NotificationsRequestEventPayload(
                        order_id=ORDER_ID,
                        order=smn.OrderEvent(original_order_id=ORDER_ID,
                                             positions=[smn.OrderEventPositionsInner(id='6486',
                                                                                     quantity=1,
                                                                                     weight=''),]),
                    )
            )
            req = smn.models.NotificationsRequest(event=_event)
            print(req)
            api_response = await self.api.notifications(notifications_request=req, api_version='3.0')

        except smn.ApiException as e:
            print(f"Exception when calling {self.api.__class__.__name__} : {e}")

            # self.assertIsInstance(api_response, smn.models.ErrorsObject)

        if api_response is not None:
            print(api_response.to_str())


if __name__ == '__main__':
    unittest.main()
