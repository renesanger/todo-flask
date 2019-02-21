from flask import Flask, render_template, redirect, url_for, request, make_response
import os
import json
from pprint import pprint
from StringIO import StringIO
import requests

app = Flask(__name__, static_url_path='/static')
#fruits1 = ["apple", "oranges", "bananas"]


@app.route('/')
def index():
	return render_template('cook.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   	if request.method == 'POST':
   		user = request.form['nm']
   
   	cookies = {'username': 'james'}

   	   	#cookies = dict(cookies_are='working')
   	r = requests.post('https://hunter-todo-api.herokuapp.com/auth', cookies=cookies)

   	return render_template('readcookie.html')

@app.route('/getcookie')
def getcookie():
	username = request.cookies.get('username')
   # name = request.cookies['username']
   # return '<h1>welcome '+name+'</h1>'
   	return username

@app.route('/todo')
def todo():
   	url = 'https://hunter-todo-api.herokuapp.com/todo-item'
	r = requests.get(url)
	
   # name = request.cookies['username']
   # return '<h1>welcome '+name+'</h1>'
   	return redirect(url_for('list'))


@app.route('/about')
def about():
	return render_template('index.html')

@app.route('/list')
def list():
	with open('data.json') as file:
		data = json.load(file)
		data = json.dumps(data)

		io = StringIO()
		json.dump(data, io)

	return render_template('list.html', data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['user']
		return render_template("result.html", user = username)

	return render_template('login.html')

@app.route('/logout')
def logout():
	return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['user']
		url = 'https://hunter-todo-api.herokuapp.com/user'
		data = {"username" : username}
		data_json = json.dumps(data)
		headers = {'Content-type': 'application/json'}

		response = requests.post(url, data=data_json, headers=headers)
	 	return redirect(url_for('todo'))

	return render_template('register.html')
		
@app.route('/api')
def api():
	r = requests.get('https://hunter-todo-api.herokuapp.com/user')
	obj = r.text
	return obj


# @app.route('/')
# def home(fruits = fruits1):
# 	return render_template('home.html', fruits=fruits)



if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, threaded=True)

"""
NOTES

FLask: basic web framework for python
MVC: Model View Controller

for this example we do not need to worry about models
controller exists in app.py


"""

