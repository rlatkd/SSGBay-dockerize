from pymysql import connect
import datetime
import shutil
from flask import Flask, json, jsonify
from os import path
import pymysql


connectionString = {
    'host': 'mysql',
    'port': 3306,
    'database': 'auction',
    'user': 'user1',
    'password': '1234',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}

def idCheck(user_id, pwd):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            sql = "SELECT * FROM user " + "where id = %s and password = %s;"
            cursor.execute(sql, [user_id, pwd])
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        
def getMyItem(user_id):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            sql = "SELECT * FROM item where user_id = %s;"
            cursor.execute(sql, [user_id])
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)        

def getItems(sort, keyword):
    try:
        query = "SELECT * FROM item"
  
        # Conditionally filter by keyword
        if keyword:
            query += f" WHERE name LIKE '%{keyword}%' OR content LIKE '%{keyword}%'"
                
        if sort == "priceDown":
            query += " ORDER BY price DESC"
        elif sort == "priceUp":
            query += " ORDER BY price ASC"
        else:
            query += " ORDER BY startTime DESC"
            
        with connect(**connectionString) as con:
            cursor = con.cursor()
            cursor.execute(query)
            itemInfo = cursor.fetchall()
            cursor.close()
            
            # columns = [desc[0] for desc in cursor.description]
            # data = [dict(zip(columns, row)) for row in user_info]
        if not itemInfo:
            return [], 200, { 'Content-Type': 'application/json'}

        return itemInfo, 200, { 'Content-Type': 'application/json'}


    except Exception as e:
        print(e)


# 메인페이지에서 1번상품을 들어가면 1번상품에 해당하는 내용이 나와야하기떄문에 id인자와 쿼리문 살짝 수정
def getItemDetails(id):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            sql = "select * from item where id = %s"
            cursor.execute(sql, (id, ))
            itemDetails = cursor.fetchone()
            cursor.close()
            
            # columns = [desc[0] for desc in cursor.description]
            # data = [dict(zip(columns, row)) for row in user_info]
        return itemDetails, 200, { 'Content-Type': 'application/json'}

    except Exception as e:
        print(e)
        
        
def addUserInfo(userId, userPwd, userNickname, userPhone):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            sql = f"""INSERT INTO user (id, password, nickname, phone) VALUES("{userId}","{userPwd}","{userNickname}","{userPhone}")"""
            print(cursor.execute(sql))
            userInfo = cursor.fetchall()
            con.commit()
        
        return userInfo, 200, { 'Content-Type': 'application/json'}    
            
    except Exception as e:
        print(e)

# 마이페이지에서 내 게시글 내역
def getMyItem(user_id):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            sql = "SELECT * FROM item where user_id = %s;"
            cursor.execute(sql, [user_id])
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e) 
                
# 마이페이지에서 내 구매내역
def getBuyItem(user_id):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            # user_id로 history item_id를 조회하고, 조회된 item_id로 item테이블의 데이터를 출력하는 쿼리
            # sql = "SELECT * from history where user_id = %s;"
            sql = "SELECT item.* FROM item INNER JOIN history ON item.id = history.item_id WHERE history.user_id = %s;"
            cursor.execute(sql, [user_id])
            result = cursor.fetchall()
            print(result)
            return result
    except Exception as e:
        print(e)        
# # 마이페이지에서 내 구매내역
# def getBuyItem(id):
#     try:
#         with connect(**connectionString) as con:
#             cursor = con.cursor()
#             sql = "SELECT * FROM history where user_id = %s;"
#             cursor.execute(sql, [id])
#             result = cursor.fetchall()
#             return result
#     except Exception as e:
#         print(e)  

# def getMyItem(user_id):
#     try:
#         with connect(**connectionString) as con:
#             cursor = con.cursor()
#             sql = "SELECT * FROM item where user_id = %s;"
#             cursor.execute(sql, [user_id])
#             result = cursor.fetchall()
#             return result
#     except Exception as e:
#         print(e) 

# 마이페이지에서 내 게시글        
# def getMyItem(id):
#     try:
#         with connect(**connectionString) as con:
#             cursor = con.cursor()
#             sql = "SELECT * FROM item where user_id = %s;"
#             cursor.execute(sql, [id])
#             result = cursor.fetchall()
#             return result
#     except Exception as e:
#         print(e) 
        
def addItemInfo(itemName, itemContent, itemPrice, itemImage, endTime, userId):
    
    with connect(**connectionString) as con:
            cursor = con.cursor()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(userId + "merongd")
            # SQL 쿼리 수정: 플레이스홀더를 사용하여 SQL 인젝션을 방지합니다.
            sql = "INSERT INTO item (name, content, price, image, endTime, startTime, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (itemName, itemContent, itemPrice, itemImage, endTime, now, userId))
            con.commit()

    return "경매물품 등록 성공", 200
    # try:
    #     with connect(**connectionString) as con:
    #         cursor = con.cursor()
    #         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #         print(userId + "merongd")
    #         # SQL 쿼리 수정: 플레이스홀더를 사용하여 SQL 인젝션을 방지합니다.
    #         sql = "INSERT INTO item (itemName, itemContent, itemPrice, itemImage, endTime, startTime, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    #         cursor.execute(sql, (itemName, itemContent, itemPrice, itemImage, endTime, now, userId))
    #         con.commit()

    #     return "경매물품 등록 성공", 200

    # except Exception as e:
    #     print(e)
    #     return "요청 중 오류가 발생", 500   

# database.py
def getItemDetails(id):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            sql = "select * from item where id = %s"
            cursor.execute(sql, (id, ))
            itemDetails = cursor.fetchone()
            cursor.close()
            
            # columns = [desc[0] for desc in cursor.description]
            # data = [dict(zip(columns, row)) for row in user_info]
        return itemDetails, 200, { 'Content-Type': 'application/json'}

    except Exception as e:
        print(e)
        
def updatePrice(id, price, new_price):
    try:
        with connect(**connectionString) as con:
            cursor = con.cursor()
            sql = "UPDATE item SET price = %s WHERE id = %s"
            cursor.execute(sql, (new_price,id))
            con.commit()
            cursor.close()
            return {"message": "입찰되었습니다."}, 200

    except Exception as e:
        print(e)
        return {"message": "가격 업데이트에 실패했습니다."}, 500