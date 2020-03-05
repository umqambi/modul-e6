# -*- coding: utf-8 -*-
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!!!"

@app.route('/ru/')
@app.route('/ru/index')
def ruindex():
    return "Привет, Мир!"