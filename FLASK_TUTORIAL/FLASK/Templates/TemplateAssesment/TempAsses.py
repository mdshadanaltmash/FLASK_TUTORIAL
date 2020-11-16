from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/report')
def report():
    username=request.args.get('uname')
    lcase=False
    ucase=False
    num_end=False

    lcase=any(x.islower() for x in username)
    ucase=any(x.isupper() for x in username)
    num_end=username[-1].isdigit()

    report=lcase and ucase and num_end
    if report:
        return render_template('report.html',status=report)
    else:
        reports=[]
        if lcase==False:
            reports.append("Sorry you don't have any lowercase letter in your username.")
        if ucase==False:
            reports.append("Sorry you don't have any Uppercase letter in your username.")
        if num_end==False:
            reports.append("Sorry your username does not end with Digit.")
        return render_template('report.html',status=report, reasons=reports)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
