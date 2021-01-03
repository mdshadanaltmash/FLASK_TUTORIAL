from werkzeug import generate_password_hash,check_password_hash
from flask_bcrypt import Bcrypt
############ Using werkzeug ##################
hashed_pass=generate_password_hash('mypassword')
print(hashed_pass)
print(check_password_hash(hashed_pass,'notmypass'))

########### Using Bcrypt ####################

bcrypt=Bcrypt()
password='mypassword'
hashed_pass=bcrypt.generate_password_hash(password=password)
print(hashed_pass)
print(bcrypt.check_password_hash(hashed_pass,'notmypass'))
