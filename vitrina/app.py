from flask import Flask, abort, render_template

app = Flask(__name__)

DRINKS = {
    "cappuccino": {
        "name": "Капучино",
        "price": 180,
        "volume": 250,
        "description": "Эспрессо со взбитым молоком и плотной молочной пеной.",
    },
    "cocoa": {
        "name": "Какао",
        "price": 150,
        "volume": 300,
        "description": "Горячий шоколадный напиток на молоке.",
    },
}


@app.get("/")
def menu():
    return render_template("menu.html", drinks=DRINKS)


@app.get("/drinks/<slug>")
def drink_detail(slug):
    drink = DRINKS.get(slug)
    if drink is None:
        abort(404)
    return render_template("drink.html", drink=drink)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
