from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app  = Flask(__name__)



# DB Congif using sqlLite

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# Initilize db
db=SQLAlchemy(app)


# Define database Model

class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(180), nullable=False)
    status=db.Column(db.String(100))

    def __repr__(self):
        return f"Todo('{self.description}) - Status'{self.status}')"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/todos')
def listTodos():
    todos=Todo.query.all()
    return render_template('todoList.html',todos=todos)

    
if __name__ == '__main__':
    app.run(debug=True, port=8000)