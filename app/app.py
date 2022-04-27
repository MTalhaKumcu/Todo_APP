from re import A
from tokenize import Triple
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/MehmetKumcu/Desktop/app/app.db'
db = SQLAlchemy(app)
#index
@app.route("/")
def index():
    todos= App.query.all()
    return render_template("index.html",todos=todos)

@app.route("/complete/<string:id>")

def completeTodo (id):
    todo = App.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/detele/<string:id>")
def deleteTodo(idd):
    todo = App.query.filter_by(idd=idd).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
""" 
if todo.complete == True:
todo.complete == False
else:
todo.complete == True
"""
#add

@app.route("/add" , methods=["POST"])
def addTodo():  
    title =request.form.get("title")
    newTodo = App(title = title,complete = False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))



class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__=="__main__":
    db.create_all()
    app.run(debug =True)