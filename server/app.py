from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
app = Flask(__name__)


# messages = [] # a pretend database
# users = []
colors = ["purple", "red", "green", "blue", "yellow", "pink"]


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/message', methods=['POST'])
def create_message():
    mc=MongoClient()
    db=mc.test
    coll=db.messages
    collUser=db.users
    json_body = request.get_json()
    print(json_body)
    if 'text' in json_body:
        message={
            'message': json_body["text"],
            'user': json_body["user"]
        }
        # messages.append(message)
        coll.insert(message)
        # if message["user"] not in users:
        users=list(collUser.find())
        userStrings=[u["user"] for u in users]
        if message["user"] not in userStrings:
            # users.append(message["user"])
            collUser.insert({'user': message["user"]})
    return 200


@app.route('/getMessages', methods=['GET'])
def get_messages():
    mc=MongoClient()
    db=mc.test
    coll=db.messages
    collUser=db.users
    messagesList = list(coll.find())
    for m in messagesList:
        m["_id"] = str(m["_id"])
    usersList = list(collUser.find())
    for u in usersList:
        u["_id"] = str(u["_id"])
    # json_body = {'messages': messages, "users": users, "colors": colors,}
    json_body = {'messages': messagesList, "users": usersList, "colors": colors,}
    print(json_body)
    return jsonify(json_body)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
