import time

from django.core.exceptions import PermissionDenied


class DelayMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time.sleep(0)
        response = self.get_response(request)

        return response
