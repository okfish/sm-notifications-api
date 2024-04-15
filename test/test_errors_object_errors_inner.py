# coding: utf-8


import unittest

from sm_notifications_api.models.errors_object_errors_inner import ErrorsObjectErrorsInner

class TestErrorsObjectErrorsInner(unittest.TestCase):
    """ErrorsObjectErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorsObjectErrorsInner:
        """Test ErrorsObjectErrorsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorsObjectErrorsInner`
        """
        model = ErrorsObjectErrorsInner()
        if include_optional:
            return ErrorsObjectErrorsInner(
                type = 'unprocessable_entity',
                field = 'name',
                message = 'не может быть пустым'
            )
        else:
            return ErrorsObjectErrorsInner(
                type = 'unprocessable_entity',
                field = 'name',
                message = 'не может быть пустым',
        )
        """

    def testErrorsObjectErrorsInner(self):
        """Test ErrorsObjectErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
