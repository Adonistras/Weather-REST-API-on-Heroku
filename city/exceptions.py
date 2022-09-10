from rest_framework.exceptions import APIException

class CityDoesNotExists(APIException):
    status_code = 404
    default_code = 'City not found'
    default_detail = 'City not found, try again'