from flask import Flask, request


app = Flask(__name__)

@app.route('/test', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.origin, request.get_json(), sep=": ")
        return '{"success":true}'
    else:
        print(request.origin)
        return "test"


if __name__ == "__main__":
    app.run()
