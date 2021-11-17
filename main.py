from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/flv')
def player():
    return render_template("flv.html")

@app.route('/m3u8')
def m3u8():
    return render_template("m3u8.html")

if __name__ == '__main__':
    app.run('0.0.0.0')
