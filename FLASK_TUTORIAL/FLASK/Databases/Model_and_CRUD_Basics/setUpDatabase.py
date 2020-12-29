from basic import db,Puppy

#Creates all the Table Models
db.create_all()

sam=Puppy('sams',3)
frank=Puppy('franky',4)

print(sam.id,frank.id)

db.session.add_all([sam,frank])
db.session.commit()

print(sam.id,frank.id)
