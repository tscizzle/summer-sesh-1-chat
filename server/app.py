from flask import Flask, request, render_template, jsonify
app = Flask(__name__)


messages = [] # a pretend database


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/message', methods=['POST'])
def create_message():
    json_body = request.get_json()
    if 'text' in json_body:
        messages.append(json_body['text'])
    return 200


@app.route('/getMessages', methods=['GET'])
def get_messages():
    json_body = {'messages': messages}
    return jsonify(json_body)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
