from basic import db, Puppy

####CREATE####
jhon=Puppy('jhonny',7)
db.session.add(jhon)
db.session.commit()


####READ####

all_puppies=Puppy.query.all() #list of puppy object
print(all_puppies)

#get by id
id=8
puppy_one=Puppy.query.get(id)
print(puppy_one.name)
print(puppy_one)

#Filters
puppy_filtered=Puppy.query.filter_by(name= '%jhonny%')
print(puppy_filtered.all()) #prints lists of all the query output

####UPDATE####
first_puppy=Puppy.query.get(1)
first_puppy.age=9
db.session.add(first_puppy)
db.session.commit()

####DELETE####
id =7
get_puppy=Puppy.query.get(id)
db.session.delete(get_puppy)
db.session.commit()

##Print##
all_puppies=Puppy.query.all()
print(all_puppies)
