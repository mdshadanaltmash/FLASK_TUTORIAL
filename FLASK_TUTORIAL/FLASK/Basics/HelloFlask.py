from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Shadan, <br> Keep Trying</h1>"
@app.route('/some')
def some():
    return "<h1>Well done Shadan, <br> Keep Trying Some</h1>"

@app.route('/some/<name>')
def someName(name):
    return (f"<h1>Hello {name}, <br> Keep Trying</h1>")


if __name__=='__main__':
    app.run()
