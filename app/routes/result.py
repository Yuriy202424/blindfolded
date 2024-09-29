from flask import render_template, request
from sqlalchemy import select

from ..db import Session, User
from app import app


@app.get('/result')
def result():
    with Session.begin() as session:
        username = session.scalar(select(User.username))
    return render_template("result.html", username=username)