from app import app, db
from flask import Flask , render_template, url_for, request,redirect
from .models import Player, World
from .functions import *

@app.route('/',methods = ['POST','GET'])
def index():
    player = generate_player()
    if request.method == 'POST':
        new_id = request.form['ID_Input']
        new_task = Player(id=new_id)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Player.query.order_by(Player.id).all()
        print(player)
        return render_template('base.html',player = player)

@app.route('/delete/<string:id>',)
def delete(id):
    task_to_delete = Player.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
    

@app.route('/update/<string:id>', methods= ['POST','GET'])
def Update(id):
    task = Player.query.get_or_404(id)

    if request.method == 'POST':
        task.id = request.form['ID_Input']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        return render_template('display.html', task = task)
    
