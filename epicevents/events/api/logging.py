import logging


logger = logging.getLogger(__name__)


class APILogMiddleware:
    """
    This middleware add information to the logger about the requests processed
    by the API.
    It logs all requests that succesfully modify the data of the database.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = str(request.user)
        method = str(request.method).upper()
        status_code = str(response.status_code)
        path = str(request.path)
        if method == 'POST':
            data = str(dict(request.POST.items()))
        elif method == 'PUT':
            data = str(dict(request.PUT.items()))
        if method in ('POST', 'PUT') and path != '/auth-token/' and (status_code.startswith('2')):
            message = f"{user}: {method} {path} {status_code} {data}"
            logger.info(message)
        return response


class EpicEventsLogFormatter(logging.Formatter):
    default_time_format = '%d/%b/%Y %H:%M:%S'
