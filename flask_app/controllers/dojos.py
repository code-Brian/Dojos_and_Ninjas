from flask import Flask, render_template, redirect, session, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    print('controller index called')
    return render_template('dojo_create.html', dojos=dojos)

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    print('creating a new dojo')
    # do some stuff here to create a data dictionary. 
    data = {
        'dojo_name': request.form.get('dojo_name')
    }
    Dojo.save(data)
    print(f'Dojo is: {data}')
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_ninjas(id):
    data = {
        'id' : id,
    }
    print('showing all the ninjas in the dojo')
    return render_template('dojo_ninjas.html', dojo = Dojo.get_one(data), ninjas = Ninja.get_dojo_ninjas(data))
