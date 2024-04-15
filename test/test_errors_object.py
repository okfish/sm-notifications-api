# coding: utf-8


import unittest

from sm_notifications_api.models.errors_object import ErrorsObject

class TestErrorsObject(unittest.TestCase):
    """ErrorsObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorsObject:
        """Test ErrorsObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorsObject`
        """
        model = ErrorsObject()
        if include_optional:
            return ErrorsObject(
                errors = [
                    sm_notifications_api.models.errors_object_errors_inner.errors_object_errors_inner(
                        type = 'unprocessable_entity',
                        field = 'name',
                        message = 'не может быть пустым', )
                    ],
                code = 422
            )
        else:
            return ErrorsObject(
                errors = [
                    sm_notifications_api.models.errors_object_errors_inner.errors_object_errors_inner(
                        type = 'unprocessable_entity',
                        field = 'name',
                        message = 'не может быть пустым', )
                    ],
                code = 422,
        )
        """

    def testErrorsObject(self):
        """Test ErrorsObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
