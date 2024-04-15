# coding: utf-8
from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "sm-notifications-api"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.0",
    "python-dateutil",
    "aiohttp >= 3.0.0",
    "aiohttp-retry >= 2.8.3",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Sbermarket Orders API Notifications [RTE]",
    author="Oleg Rybkin aka Fish with help of OpenAPI Generator community",
    author_email="okfish@yandex.ru",
    url="",
    keywords=["asyncio", "aiohttp","OpenAPI", "OpenAPI-Generator", "Sbermarket Orders API Notifications [RTE]"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Данная спецификация описывает API, который должен вызываться Партнёром в рамках процесса работы
    с ready-to-eat заказами.
    В случае, если Партнёр работает в режиме собственной сборки только для самовывоза,
    данный API должен использоваться только для заказов, у которых выбран тип доставки
    &#x60;pickup&#x60; (самовывоз)
    При работе с данным API нужно дополнительно передавать HTTP заголовок
    &#x60;Api-Version: 3.0&#x60; во все запросы уведомлений.
    Для аутентификации необходимо к запросу добавить заголовок client-token со значением токена,
    полученным в разделе “Получение токена”
    """,  # noqa: E501
    package_data={"sm_notifications_api": ["py.typed"]},
)
