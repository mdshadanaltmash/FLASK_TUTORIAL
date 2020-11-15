from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    squares=[x**2 for x in range(10)]
    names=['Md','Shadan','Altmash']
    return render_template('controlFlow.html',squares=squares,names=names)

if __name__=='__main__':
    app.run(debug=True)
