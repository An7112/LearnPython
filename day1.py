from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Thiết lập kết nối với MongoDB
client = MongoClient("mongodb+srv://thanhan7112:123456789An@cluster0.wjfi1q5.mongodb.net/?retryWrites=true&w=majority")
db = client['python_database']
collection = db['users']

# Route mặc định
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the API!'
    })

# Route lấy danh sách users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    serialized_users = []
    for user in users:
        serialized_user = {
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email']
        }
        serialized_users.append(serialized_user)
    return jsonify(serialized_users)

# Route tạo người dùng mới
@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    collection.insert_one(user)
    serialized_user = {
        'id': str(user['_id']),
        'name': user['name'],
        'email': user['email']
    }
    return jsonify(serialized_user), 201

if __name__ == '__main__':
    app.run()
