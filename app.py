from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
# from pymongo import MongoClient
# The Following code ia my own 
uri = "mongodb+srv://FMuser:KoolWordz@cluster0.ykezvyd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['priority']
        todos.insert_one({'content': content, 'priority': degree})
        return redirect(url_for('index'))
    
    # find all todos in mongodb database
    all_todos_object = list(todos.find())

    print(all_todos_object)

    all_todos = todos.find()

    # give all the todos to the 'index.html' template
    return render_template('index.html', todos=all_todos_object)

coustom_priority_order ={'Very Important': 1,
                         'Important': 2, 'Normal': 3, 'Uniportant': 4}



if __name__ == '__main__':
    app.run(debug=True, port=5002)

# KoolWordz