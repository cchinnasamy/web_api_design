from api import API, response
from werkzeug.serving import run_simple

app = API()


@app.route("/home")
def home(request):
    name = request.args.get("name", "?")
    text = f"Hello {name}"
    return response(text)


@app.route("/home/{who}")
def home(request, who):
    text = f"Hello {who}"
    return response(text)


if __name__ == "__main__":
    run_simple('127.0.0.1', 8000, app, use_debugger=True, use_reloader=True)