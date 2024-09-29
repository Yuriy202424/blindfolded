from datetime import datetime

from flask import render_template, request

from ..db import Session, User
from app import app


@app.get('/')
def register():
    return render_template('register.html')


@app.post('/')
def get_data():
    date = datetime.now()
    username = request.form.get("username")
    password = request.form.get("password")
    fav_word = request.form.get("fav_word")
    print("*" * 80)
    print(date)
    print(username)
    print(password)
    print(fav_word)
    with Session.begin() as session:
        user = User(date=date, username=username, password=password, fav_word=fav_word)
        session.add(user)
    return render_template('result.html')