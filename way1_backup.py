# app.py

from api import API, Response

app = API()


@app.route("/home")
def home(request):
    name = request.params.get("name", "?")
    response = Response()
    response.text = f"Hello {name}"
    return response


@app.route("/home/{who}")
def home(request, who):
    response = Response()
    response.text = f"Hello {who}"
    return response


# api.py
from parse import parse
from webob import Request, Response


class API:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)

        return response(environ, start_response)

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named

        return None, None

    def handle_request(self, request):
        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            response = handler(request, **kwargs)
        else:
            response = self.default_response()

        return response

    def default_response(self,):
        response = Response()
        response.status_code = 404
        response.text = "Not found."
        return response
