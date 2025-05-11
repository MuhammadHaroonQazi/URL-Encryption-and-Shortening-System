
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    print("FILES:", os.listdir("templates"))
    return render_template("index.html")

@app.route('/decrypt')
def decrypt():
    return render_template("decrypt.html")

if __name__ == "__main__":
    app.run(debug=True)
