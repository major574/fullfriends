from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector('friendsdb')

@app.route('/', methods=['GET'])
def index():
    friends = mysql.fetch("SELECT * FROM friends")
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
    print query
    mysql.run_mysql_query(query)
    return redirect('/')   

@app.route('/friends/<int:id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET occupation = '{}', first_name = '{}', last_name = '{}' WHERE id = {}".format(request.form['occupation'], request.form['first_name'], request.form['last_name'], id)
    print query
    mysql.run_mysql_query(query)
    return redirect('/')


@app.route('/friends/<int:id>/edit', methods=['GET'])
def edit(id):
    friend = mysql.fetch("SELECT * FROM friends WHERE id = " + str(id))
    print friend
    return render_template('edit.html', friend=friend[0])   

@app.route('/friends/<int:id>/delete', methods=['POST'])
def destroy(id):
    delete = "DELETE FROM friendsdb.friends WHERE id = {}".format(id)
    mysql.run_mysql_query(delete)
    return redirect('/')

app.run(debug=True)

