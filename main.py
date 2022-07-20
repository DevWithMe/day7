from flask import Flask, render_template, request, redirect

app = Flask(__name__)

items = []

@app.route('/')
def index():
  print(items)
  return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
  global items
  if request.method == "POST":
    item = request.form.get("item")
    items.append(item)
    print(items)
    return redirect("/")

@app.route("/delete/<string:item>")
def delete_item(item):
  global items
  items.remove(item)
  return redirect("/")

app.run(host='0.0.0.0', port=81)