class DebugHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Incoming HOST header:", request.META.get("HTTP_HOST"))
        return self.get_response(request)
