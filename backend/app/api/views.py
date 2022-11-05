from email import message

from . import api
from flask import jsonify, request, redirect, url_for
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from .models import User, user_schema, users_schema
from app import db, bcrypt


@api.route('/v1/login', methods=['POST'])
def login():
    if request.is_json: # if a json
        req_username = request.json.get("req_username", None)
        req_password = request.json.get("req_password", None)
    else: # if submitted as a form
        req_username = request.form["req_username"]
        req_password = request.form["req_password"]        
    if not req_username:
        return jsonify({"msg": "Bad username or password"}), 401
    user = User.query.filter_by(username=req_username).one_or_none()
    if user:
        if bcrypt.check_password_hash(user.password_hash, req_password):
            access_token = create_access_token(identity=req_username)
            return jsonify(
                {
                    "access_token" : access_token,
                    "id" : user.id,
                    "username" : user.username }), 200
        else:
            return jsonify(message="invalid password"), 401
    else:
        return jsonify(message="invalid user"), 401
    
# TODO: use mailtrap.io to enable email password reset
# FIXME: 

# fetch logged in user
@api.route('/v1/user')
@jwt_required()
def user():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    return jsonify(user=user), 200



@api.route('/v1/register', methods=['POST'])
def register():
    username = request.json.get("username", None)
    check = User.query.filter_by(username=username).first()
    if check:
        return jsonify(message='Username already exists.'), 409
    else:
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        
    user = User(
        username=username.lower(),
        password=password,
        email=email.lower())
    try:
        db.session.add(user)
    except:
        return 400
    db.session.commit()
    return jsonify(message="User successfully created"), 201


# TODO: a route for returning a single user


@api.route('/v1/users')
@jwt_required()
def users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result), 200

