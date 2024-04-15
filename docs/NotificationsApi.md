# sm_notifications_api.NotificationsApi

All URIs are relative to *https://api.sbermarket.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications**](NotificationsApi.md#notifications) | **POST** /v1/notifications | Отправка события


# **notifications**
> notifications(api_version, client_token, notifications_request)

Отправка события

Отправка события

### Example

* Api Key Authentication (client_token_auth):

```python
import sm_notifications_api
from sm_notifications_api.models.notifications_request import NotificationsRequest
from sm_notifications_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sbermarket.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = sm_notifications_api.Configuration(
    host = "https://api.sbermarket.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: client_token_auth
configuration.api_key['client_token_auth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['client_token_auth'] = 'Bearer'

# Enter a context with an instance of the API client
async with sm_notifications_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sm_notifications_api.NotificationsApi(api_client)
    api_version = '3.0' # str | Версия API
    client_token = 'qwerty123sbermarket' # str | Токен клиента
    notifications_request = {"event":{"type":"order.accepted","payload":{"order_id":"H1234567890","orderUUID":"265cb601-a78a-4862-9e9d-d6b48d6a0a3f"}}} # NotificationsRequest | 

    try:
        # Отправка события
        await api_instance.notifications(api_version, client_token, notifications_request)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| Версия API | 
 **client_token** | **str**| Токен клиента | 
 **notifications_request** | [**NotificationsRequest**](NotificationsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[client_token_auth](../README.md#client_token_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Событие обработано |  -  |
**202** | Событие уже было обработано |  -  |
**401** | unauthorized |  -  |
**422** | Требуемые данные отсутствуют или некорректны |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

