from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/myself")
def about():
    return render_template("myself.html")

#if __name__ == "__main__":
    #app.run()
