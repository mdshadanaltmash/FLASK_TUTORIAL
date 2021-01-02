#set up the db inside the __init__.py under myproject
from myproject import db
class Puppy(db.Model):
    __tablename__='puppies'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    #One to One
    #one Puppy----> one Owner
    owner=db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.owner:
            return f"Puppy id is {self.id }, Puppy name is {self.name} and the owner name is {self.owner.name}."
        else:
            return f"Puppy id is {self.id}, Puppy name is {self.name} and has no owner yet."


class Owner(db.Model):
    __tablename__='owners'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id=puppy_id
    def __repr__(self):
        return f"Owner: {self.name}"
