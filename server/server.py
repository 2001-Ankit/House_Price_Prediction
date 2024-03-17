from flask import Flask, request, jsonify


app = Flask(__name__)


import util


@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_house_price", methods=["GET", "POST"])
def predict_house_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify(
        {"estimated_price": util.get_estimate_price(location, total_sqft, bhk, bath)}
    )
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response


if __name__ == "__main__":
    print("Flask ready")
    util.load_save_artifacts()
    app.run(debug=True)
