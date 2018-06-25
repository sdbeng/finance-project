from flask import Flask, request
from datetime import datetime
# from pytz import timezone

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World Cup!!'

@app.route('/mytime')
# def time():
#     now = datetime.now(timezone('America/New_York'))
#     return "The current date and time in Cambridge is {}".format(now)


@app.route("/show/<number>")
def show(number):
    return "You passed in {}".format(number)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # do one thing
        print("goes for post")
    else:
        # do a different thing
        print("goes for post")

        # run main
if __name__ == "__main__":
    app.run()
