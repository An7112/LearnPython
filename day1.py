from flask import Flask, jsonify, request

app = Flask(__name__)

#Route mặc định
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the API!'
    })
#Route lấy danh sách users
@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {'_id': 1, 'name': 'Nguyen Thanh An'}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run()