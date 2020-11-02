from sanic import Sanic
from sanic.response import json
from sanic_jwt import Initialize
from sanic_jwt.decorators import protected
from auth import authenticate_csv


app = Sanic("Polyrize Backend Assignment")
Initialize(app, authenticate=authenticate_csv)


@app.route("/normalize", methods=['POST'])
@protected()
def normalize(request):
    payload = request.json
    data = payload["data"]
    normalized = {d['name']: d[[key for key in d.keys() if 'Val' in key][0]] for d in data}
    return json(normalized)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
