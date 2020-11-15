from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello<br></h1><h3> Append the string at the end of url to play simple latin name game</h3>"

@app.route('/<name>')
def latinName(name):
    nameLatin=''
    if name[-1]=='y':
        #print(name[-1])
        nameLatin=name[0:-1]+'iful'
    else:
        nameLatin=name+"y"
    return (f"<h1>Hello {name}, your latin name is {nameLatin}, <br> Keep coming back</h1>")


if __name__=='__main__':
    app.run()
