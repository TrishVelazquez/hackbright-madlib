"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Ask if want to play mad libs - if yes go to mad libs form"""

    ans = request.args.get("yesno")

    if ans == "yes":
        return render_template("game.html")

    return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Shows finished mad libs text"""
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective",)

    madlibs = ["madlib.html", "madlib1.html", "madlib2.html"]
    madlib = choice(madlibs)

    return render_template(madlib,
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
