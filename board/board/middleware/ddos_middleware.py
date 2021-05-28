import time

from django.core.exceptions import PermissionDenied


class DDosMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0


    def __call__(self, request):


        if self.count >= 2:
            raise PermissionDenied




        ip = request.META.get('REMOTE_ADDR')
        response = self.get_response(request)
        self.count += 1




        return response
