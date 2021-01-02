Steps to do Migrate
1. from flask_migrate import Migrate
2. After creating your app and db, call Migrate class with your app and db as parameters. e.g Migrate(app,db)
3. save
4. in cmd
  a. set FLASK_APP=filename.py (your main file name)
  b. flask db init
  c. flask db migrate -m "your message"
  d. flask db upgrade


Now if you do any changes then you will have to below Steps
1. save the changes
2. db migrate -m "your message"
3. flask db upgrade
