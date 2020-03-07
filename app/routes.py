# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app, cache
from app.forms import NumFiboForm
from app.utils import is_positiv_integer, fibonacci

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
                cache.set(number, fibo_for_number)
                return render_template('fibo.html', number=number, fibo_for_number=fibo_for_number)
            else:
                fibo_for_number_cached = cache.get(number)
                return render_template('fibo.html', number=number, fibo_for_number=fibo_for_number_cached)
        else:
            form1 = NumFiboForm()
            return render_template('fibo.html', not_integer = True, form1=form1)