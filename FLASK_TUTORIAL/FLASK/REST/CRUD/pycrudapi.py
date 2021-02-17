from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)
empNames=[]

class Employee(Resource):
    def get(self,name):
        for emp in empNames:
            if emp['Name']==name:
                return({'Name':name})
        else:
            return {'Name':None},404
    def post(self,name):
        emp={'Name':name}
        empNames.append(emp)
        return (emp)
    def delete(self,name):
        for idx,emp in enumerate(empNames):
            if emp['Name']==name:
                deleted_emp=empNames.pop(idx)
                return(deleted_emp ,"deleted successfully")
        else:
            return ({name:'Not Found'} ,404)

class AllEmployee(Resource):
    def get(self):
        return{'employee Name': empNames}

api.add_resource(Employee,'/emp/<string:name>')
api.add_resource(AllEmployee,'/employees')

if __name__=='__main__':
    app.run(debug=True)
