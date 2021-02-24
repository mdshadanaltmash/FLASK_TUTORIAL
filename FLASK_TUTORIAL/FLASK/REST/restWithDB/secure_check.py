from users import Users

users=[Users(1,'Md','mysecret'),Users(2,'Shadan','secret'),Users(3,'Altmash','password')]

username_table={u.username: u for u in users}
userid_table={u.id: u for u in users}

def authenticate(username,password):

    user=username_table.get(username,None)
    if user and password==user.password:
        return user

def identity(payload):
    user_id=payload['identity']
    return userid_table.get(user_id,None)
