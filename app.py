from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def test():
        
    response = {
        "message": "it works!"
    }
    return jsonify(response)
    
@app.route('/multiply_by_2/<number>')
def multiply_by_2(number):
    try:
        number = int(number)
        response = {
            "message": "Here is the response!",
            "res": number * 2 
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed'}), 400

@app.route('/multiply_x_times_y', methods = ['POST'])
def multiply_x_times_y():
    res = request.get_json()

    try:
        response = {
            "message": "Here is the response!",
            "res": res["x"] * res["y"]
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed'}), 400

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8080)