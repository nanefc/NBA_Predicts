import numpy as np
from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)
modelo = pickle.load(open('notebook/modelo.pkl', 'rb'))


@app.route("/")
def verify_api_online():
    return "API ONLINE v1.0", 200


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = modelo.predict(np.array([list(data.values())]))
    result = prediction[0]

    response = {'RESULT': int(result)}
    return jsonify(response)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
