from color import GiveMeAColor
from flask import Flask, jsonify
app = Flask(__name__)

randomColor = GiveMeAColor()


@app.route("/")
def hello():
    return jsonify({"data": "tiqdev random_color_api"})


@app.route("/random", methods=['GET'])
def generateColor():
    result = randomColor.generateColor()
    return result, 200


@app.route("/randomRGB", methods=['GET'])
def generateRGB():
    result = randomColor.randomRGB()
    return jsonify({"RGB": result}), 200


@app.route("/randomHEX", methods=['GET'])
def generateHEX():
    result = randomColor.randomHex()
    return jsonify({"HEX": result}), 200


if __name__ == '__main__':
    app.run(debug=True)
