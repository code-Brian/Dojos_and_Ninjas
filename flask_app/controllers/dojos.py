from flask import Flask, render_template, redirect, session, request
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    print('controller index called')
    return render_template('dojos.html', dojos=dojos)    