from flask import Flask, request, render_template, jsonify
app = Flask(__name__)


messages = [] # a pretend database
users = []
colors = ["purple", "red", "green", "blue", "yellow", "pink"]


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/message', methods=['POST'])
def create_message():
    json_body = request.get_json()
    print(json_body)
    if 'text' in json_body:
        message={
            'message': json_body["text"],
            'user': json_body["user"]
        }
        messages.append(message)
        if message["user"] not in users:
            users.append(message["user"])
    return 200


@app.route('/getMessages', methods=['GET'])
def get_messages():
    json_body = {'messages': messages, "users": users, "colors": colors,}
    return jsonify(json_body)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
