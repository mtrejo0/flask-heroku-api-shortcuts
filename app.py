from flask import Flask, jsonify
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
        response = {
            "message": "Here is the response!",
            "res": number * 2 
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed'}), 400
if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)