from flask import Flask, jsonify, request, flash, redirect, url_for, render_template
from sqlalchemy import Column, Integer, String
from sqlalchemy.testing import db
from werkzeug.security import generate_password_hash

from server.src.main.db.init_db import get_users_for_db, create
from server.src.main.var import *

app = Flask(__name__)

# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = f'{POSTGRESQL}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST_NAME}:{POSTGRES_PORT}/{DATABASE_NAME}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/hi')
def hi():
    return 'hi'


@app.route('/user/show', methods=['GET'])
def show():
    return get_users_for_db()


@app.route('/user/create', methods=['POST'])
def add_user():
    return create()




if __name__ == "__main__":
    app.run(host=HOST_NAME, port=SERVER_PORT)
