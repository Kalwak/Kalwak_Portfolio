from Portfolio.utils import create_log


class LoggingMiddleware:
    """
    Middleware used to create a log of the users actions and save it in the database.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Log creation
        create_log(response=response, request=request)

        return response
