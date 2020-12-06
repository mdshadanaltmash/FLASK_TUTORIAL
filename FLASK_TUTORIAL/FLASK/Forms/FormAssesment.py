from flask import Flask,render_template,redirect,session,url_for,flash
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class InfoPage(FlaskForm):
    name=StringField("What is your name?")
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=InfoPage()
    if form.validate_on_submit():
        session['name']=form.name.data
        flash(f"Hi {session['name']}! Welcome to Flask learning")
        return redirect(url_for('index'))
    return render_template('index.html',form=form)

if __name__=='__main__':
    app.run(debug=True)
