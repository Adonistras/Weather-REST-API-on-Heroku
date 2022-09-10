from rest_framework.exceptions import APIException

class UserEmailNotFound(APIException):
    status_code = 404
    default_detail = 'You need to add email!'
    default_code = 'User email not found'