from flask import Flask, jsonify
from flask_cors import CORS
from api import get_google
app = Flask(__name__)
CORS(app)


@app.route('/')
def test():
        
    response = {
        "message": "it works!"
    }
    return jsonify(response)
    
@app.route('/google')
def google():
    try:
        response =  f'The google stock price is ${get_google()}'
        return jsonify(response)
        
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed'}), 400

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8080)