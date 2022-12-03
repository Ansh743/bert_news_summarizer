from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    data = {
        'msg': 'Hello'
    }
    response = jsonify(data)
    response.status_code = 200
    return response

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    data = {}

    response = jsonify(data)
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(debug=True)