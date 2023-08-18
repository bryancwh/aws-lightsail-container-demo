from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# To use local database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

# To use RDS database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<YOUR_USER>:<YOUR_PASSWORD>@<RDS_DB_ENDPOINT>:<PORT>/<DB_NAME>'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    todos = db.session.query(Todo).all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    content = request.form.get('content')

    with app.app_context():
        with db.session.begin():
            new_todo = Todo(content=content)
            db.session.add(new_todo)

    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id):    
    
    with app.app_context():
        with db.session.begin():
            todo = db.session.get(Todo, todo_id)
            todo.completed = True
            db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):

    with app.app_context():
        with db.session.begin():
            todo = db.session.get(Todo, todo_id)
            db.session.delete(todo)

    return redirect(url_for('index')) 

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run('0.0.0.0','8080')