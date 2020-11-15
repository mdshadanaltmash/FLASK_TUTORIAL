from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    name='Md Shadan Altmash'
    letters=list(name)
    name_dict={'first_name':'Md','middle_name':'Shadan','last_name':'Altmash'}
    return render_template('varTemp.html',name=name,name_dict=name_dict,letters=letters)

if __name__=='__main__':
    app.run(debug=True)
