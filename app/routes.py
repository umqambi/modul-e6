# -*- coding: utf-8 -*-
import os
from flask import render_template, request
from app import app, cache
from app.forms import NumFiboForm
from app.utils import is_positiv_integer, fibonacci

from config import Config

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/fibo/', methods=['GET', 'POST'])
def fibo():
    if request.method == 'GET':
        form = NumFiboForm()
        return render_template('fibo.html', form=form)
    
    if request.method == 'POST':
        number = request.form.get('number')
        if is_positiv_integer(number):
            if cache.get(number) is None:
                fibo_for_number = fibonacci(int(number))
                from_cache = False
                cache.set(number, fibo_for_number)
                return render_template('fibo.html', number=number, fibo_for_number=fibo_for_number, from_cache=from_cache)
            else:
                fibo_for_number_cached = cache.get(number)
                from_cache = True
                return render_template('fibo.html', number=number, fibo_for_number=fibo_for_number_cached, from_cache=from_cache)
        else:
            form1 = NumFiboForm()
            return render_template('fibo.html', not_integer = True, form1=form1)


@app.route('/testinfo')
def testinfo():
    ms = os.environ.get('MEMCACHED_SERVERS')
    config_app = Config()
    return render_template('info.html', ms=ms, config_app=config_app)