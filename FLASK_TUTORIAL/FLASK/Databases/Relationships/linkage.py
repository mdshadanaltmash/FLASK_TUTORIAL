from models import db,Puppy,Toy,Owner

rufus=Puppy('Rufus')
fido=Puppy('Fido')

#adding puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

#Check
print(Puppy.query.all())

rufus=Puppy.query.filter_by(name='Rufus').all()[0]
print(rufus)

#Create Owner
altmash=Owner('Altmash',rufus.id)

#give rufus some toys

toy1=Toy('Teddy',rufus.id)
toy2=Toy('Bell',rufus.id)

db.session.add_all([altmash,toy1,toy2])
db.session.commit()

#Grab Rufus again after above additions
rufus=Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()
