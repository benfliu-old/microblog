#
# Name: Ben Liu
# Filename: microblog.py
# Description: Main .py file, prints everything relevant stored in the database
# Citations: Miguel Grinberg Flask Mega-Tutorial - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
#

#imports
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

#MY ADDITION - prints out the id, username, and email of every user in the database
print('\nUser base:')
for user in User.query.all():
    print(str(user.id) + '.')
    print(user.username)
    print(user.email + '\n')