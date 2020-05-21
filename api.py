from parse import parse
from werkzeug.wrappers import Request, Response


def response(*args, **kwargs):
    return Response(*args, **kwargs)


class API(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)
        return self.handle_request(request)(environ, start_response)

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named

        return None, None

    def handle_request(self, request):
        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            return handler(request, **kwargs)
        else:
            return self.default_response()

    @staticmethod
    def default_response():
        return response('Not Found', status=404)
