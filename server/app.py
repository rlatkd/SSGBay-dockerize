from flask import Flask, request, jsonify
from flask_cors import CORS
import database
from os import path, remove
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
import os

app = Flask(__name__, static_folder='./resources/')
app.config["JWT_SECRET_KEY"] = "super-secret"
UPLOAD_FOLDER = path.join('.', 'resources/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def main():
    sort = request.args.get('sort')
    keyword = request.args.get('keyword')
    
    return database.getItems(sort, keyword)
    

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        userId = request.json.get('id')
        password = request.json.get('password')
        isid = database.idCheck(userId, password)
        
        if(isid) :
            access_token = create_access_token(identity=userId)
            
            return jsonify({'token': access_token, 'userId':userId}), 200
        
        else : 
            
            return jsonify({'message': '잘못된 로그인 정보입니다. 다시 입력해주세요.'}), 401
  

@app.route('/login/signup', methods=['POST'])
def signup():
    try:
        userId = request.json.get('userId')
        userPwd = request.json.get('userPwd1')
        userNickname = request.json.get('userNickname')
        userPhone = request.json.get('userPhone')
        userInfo, status_code, headers = database.addUserInfo(userId, userPwd, userNickname, userPhone)
        access_token = create_access_token(identity=userId)
        
        return jsonify({"message": "계정 추가 및 로그인 성공", "token": access_token, 'userId':userId}), 200, {'Content-Type': 'application/json'}

    except Exception as e:
        print(e)
        
        return jsonify({"message": "요청중 에러가 발생"}), 500, {'Content-Type': 'application/json'}


@app.route('/mypage/buyitem', methods=["GET"])  
def getBuyItem():
    print('구매내역 호출')
    user_id = request.args.get('id')
    
    if user_id is not None:
        user_data = database.getBuyItem(user_id)
        
        return jsonify(user_data), 200
    
    else:
        
        return jsonify({'message': '인증되지 않은 접근입니다.'}), 401 
  
      
@app.route('/mypage/myitem', methods=["GET"])  
def getMyItem():
    print('내 게시글 호출')
    user_id = request.args.get('id')
    
    if user_id is not None:
        user_data = database.getMyItem(user_id)
        
        return jsonify(user_data), 200
    
    else:
        
        return jsonify({'message': '인증되지 않은 접근입니다.'}), 401
    

@app.route('/detail/<id>', methods=['GET','PUT'])
def detail(id):
    if request.method == 'GET':
        print(database.getItemDetails(id) , id)
        
        return database.getItemDetails(id)

    if request.method == 'PUT':
        price = request.json.get('price')
        
        return database.updatePrice(id, price, new_price=price)
    

@app.route('/create', methods=['POST'])
def create():
    try:
        file = request.files['itemImage']
        filename = file.filename 
        itemName = request.form.get('itemName')
        itemContent = request.form.get('itemContent')
        itemPrice = request.form.get('itemPrice')
        itemImage = filename
        userId = request.form.get('userId')
        endTime = request.form.get('endTime')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        image_url = 'http://127.0.0.1:5000/resources/' + file.filename
        print(image_url)
        
        return database.addItemInfo( itemName, itemContent, itemPrice, image_url, endTime, userId)
              
    except Exception as e:
        print(e)
        
        return jsonify({"message": "요청중 에러가 발생"}), 500, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)