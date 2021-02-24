from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate,identity
from flask_jwt import JWT,jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)
Migrate(app,db)

jwt=JWT(app,authenticate,identity)
api=Api(app)

class EmployeeDetails(db.Model):
    name=db.Column(db.String(80),primary_key=True)

    def __init__(self,name):
        self.name=name
    def json(self):
        return({'Name':self.name})

class Employee(Resource):
    def get(self,name):
        emp=EmployeeDetails.query.filter_by(name=name).first()
        if emp:
            return emp.json()
        else:
            return {'Name':None},404
    def post(self,name):
        emp=EmployeeDetails(name=name)
        db.session.add(emp)
        db.session.commit()
        return (emp.json())
    def delete(self,name):
        emp=EmployeeDetails.query.filter_by(name=name)
        if emp:
            db.session.delete(emp)
            db.session.commit()
            return(deleted_emp ,"deleted successfully")
        else:
            return ({name:'Not Found'} ,404)

class AllEmployee(Resource):
    @jwt_required()
    def get(self):
        employees=EmployeeDetails.query.all()
        return [emp.json() for emp in employees]

api.add_resource(Employee,'/emp/<string:name>')
api.add_resource(AllEmployee,'/employees')

if __name__=='__main__':
    app.run(debug=True)
