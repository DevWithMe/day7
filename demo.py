from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
  return "Hello!"

@app.route("/hello/john")
def hello_john():
  return "<h1>Hello John!</h1>"

@app.route("/hello/boyuan")
def hello_me():
  return "<h1>Hello Boyuan!</h1>"

@app.route("/hello/<string:name>")
def hello_everyone(name):
  return f"<h1>Hello, {name}!</h1>"

app.run(host='0.0.0.0', port=81)