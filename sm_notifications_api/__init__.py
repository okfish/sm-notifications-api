# coding: utf-8

# flake8: noqa

"""
    Sbermarket Orders API Notifications [RTE]

    Данная спецификация описывает API, который должен вызываться Партнёром в рамках процесса работы
    с ready-to-eat заказами.
    В случае, если Партнёр работает в режиме собственной сборки только для самовывоза,
    данный API должен использоваться только для заказов, у которых выбран тип доставки `pickup` (самовывоз)
    При работе с данным API нужно дополнительно передавать HTTP заголовок `Api-Version: 3.0`
    во все запросы уведомлений.
    Для аутентификации необходимо к запросу добавить заголовок client-token со значением токена,
    полученным в разделе “Получение токена”

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.1.0"

# import apis into sdk package
from sm_notifications_api.api.notifications_api import NotificationsApi

# import ApiClient
from sm_notifications_api.api_response import ApiResponse
from sm_notifications_api.api_client import ApiClient
from sm_notifications_api.configuration import Configuration
from sm_notifications_api.exceptions import OpenApiException
from sm_notifications_api.exceptions import ApiTypeError
from sm_notifications_api.exceptions import ApiValueError
from sm_notifications_api.exceptions import ApiKeyError
from sm_notifications_api.exceptions import ApiAttributeError
from sm_notifications_api.exceptions import ApiException

# import models into sdk package
from sm_notifications_api.models.errors_object import ErrorsObject
from sm_notifications_api.models.errors_object_errors_inner import ErrorsObjectErrorsInner
from sm_notifications_api.models.notifications_request import NotificationsRequest
from sm_notifications_api.models.notifications_request_event import NotificationsRequestEvent
from sm_notifications_api.models.notifications_request_event_payload import NotificationsRequestEventPayload
from sm_notifications_api.models.order_event import OrderEvent
from sm_notifications_api.models.order_event_positions_inner import OrderEventPositionsInner
from sm_notifications_api.models.order_event_positions_inner_marking_code_inner import OrderEventPositionsInnerMarkingCodeInner
