from flask import Flask, render_template, redirect, request, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app.controllers import dojos
from flask_app import app

@app.route('/ninjas')
def ninjas():
    print('ninjas route ran')
    return render_template('ninja_create.html', dojos = Dojo.get_all())

@app.route('/ninja/create', methods = ['POST'])
def create_ninja():
    print('creating a new ninja')
    data = {
        'fname' : request.form.get('fname'),
        'lname' : request.form.get('lname'),
        'age' : request.form.get('age'),
        'id': request.form.get('dojo')
    }
    id = data['id']

    Ninja.add_ninja(data)

    return redirect(f"/dojos/{id}")

@app.route('/ninja/edit<int:id>')
def edit_ninja(id):
    data = {
        'id' : id
    }
    print('navigating to edit ninja page')
    return render_template('ninja_edit.html', ninja = Ninja.get_one(data), dojos = Dojo.get_all())

@app.route('/ninja/update', methods = ['POST'])
def update_ninja():
    print('upd00ting ninja')
    data = {
        'fname' : request.form.get('fname'),
        'lname' : request.form.get('lname'),
        'age' : request.form.get('age'),
        'id' : request.form.get('id'),
        'dojo_id' : request.form.get('dojo')
    }
    print(f"dojo_id is {data['dojo_id']}")
    print(f"data['id'] was {data['id']}")
    Ninja.edit_ninja(data)

    return redirect('/dojos')

@app.route('/ninja/destroy')
def destroy_ninja():
    print('destroying ninja from db...')
