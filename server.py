from flask import Flask
import random
app = Flask(__name__)

NUMBER = random.randint(0,9)


@app.route("/<int:number>")
def correct(number):
    global NUMBER
    if number == NUMBER:
        return ("<h1 style='color:green'>You guess the number!!!</h1>"
                "<img src='https://media.giphy.com/media/9xt1MUZqkneFiWrAAD/giphy.gif'>")
    elif number > NUMBER:
        return ("<h1 style='color:red'>Too high</h1>"
                "<img src='https://media.giphy.com/media/ep7lPvQMedLcwjpdh9/giphy.gif'>")
    elif number < NUMBER:
        return ("<h1 style='color:blue'>Too low</h1>"
                "<img src='https://media.giphy.com/media/0flG2X5jimIt9yVJKY/giphy.gif'>")


@app.route("/")
def hello():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/0Qk2eQBVok26h3rTFW/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)

