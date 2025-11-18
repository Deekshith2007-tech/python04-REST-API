from flask import Flask,request,jsonify
app=Flask(__name__)
users={}

@app.route('/users',methods=['GET'])
def get_all_users():
    return jsonify(users),200

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]),200
    return jsonify({"Error":"User not found"}),404


@app.route('/users',methods=['POST'])
def create_user():
    data=request.json
    user_id=data.get("id")
    name=data.get("name")
    if not user_id or not name:
        return jsonify({"Error":"id and name required"}),400
    if user_id in users:
        return jsonify({"Error":"User already exists"}),409
    users[user_id]={"id":user_id,"name":name}
    return jsonify({"Message":"user created","user":users[user_id]}),201

@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"Error":"User not found"}),404
    data=request.json
    name=request.get("name")
    if not name:
        return jsonify({"Error":"Name not found"}),400
    users[user_id]["name"]=name
    return jsonify({"message":"user  updated","user":users[user_id]}),200


@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"Error":"User not found"}),404
    del users[user_id]
    return jsonify({"Message":"user deleted"}),200

if __name__=='__main__':
    app.run(debug=True)