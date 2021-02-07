import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT']='1' #'true'
os.environ['OAUTHPATH_RELAX_TOKEN_SCOPE']='1' #'true'

from flask import Flask,render_template
from flask_dance.contrib.google import make_google_blueprint,google

app = Flask(__name__)
app.config['SECRET_KEY']='mysecret'

blueprint=make_google_blueprint(client_id='98132762827-jbd8lrlqbghp23bqp7aiv15nfjrbrc2v.apps.googleusercontent.com'
                                ,client_secret='jfxpKZcrMJHiI4WUzMVB95yU',offline=True
                                ,scope=["https://www.googleapis.com/auth/userinfo.email", "openid", "https://www.googleapis.com/auth/userinfo.profile"])
app.register_blueprint(blueprint,url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    #RETURN INTERNAL SERVER ERROR IF USER IS NOT LOGGED IN
    resp=google.get('/oauth2/v3/userinfo')
    assert resp.ok, resp.text
    email=resp.json()['email']

    return render_template('welcome.html',email=email)

@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp=google.get('/oauth2/v3/userinfo')
    assert resp.ok, resp.text

    email=resp.json()['email']

    return render_template('welcome.html',email=email)


if __name__=='__main__':
    app.run(debug=True)
