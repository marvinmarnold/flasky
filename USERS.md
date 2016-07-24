## Setup
** ALL INSTRUCTIONS SHOULD BE COMPLETED WITH VENV **
````
source venv/bin/activate
````
1. Stop your server.
2. Delete your existing database. `rm flasky.db`
3. Add db files to `.gitignore`, `echo '*.db' >> .gitignore`
4. Change `database_setup.py` to include `email` & `hashed_password` fields. Remove `id`.
````python
class Person(Base):
      __tablename__ = 'person'
      name = Column(String)
      email = Column(String, primary_key=True)
      gender = Column(String)
      nationality = Column(String)
      hometown = Column(String)
      hashed_password = Column(String)
````
5. Modify `initialize.py` to add new fields and remove unnecessary `id`. We will create the `hash_password` method next. For example:
````python
from hello import hash_password
... # <---- this means you skip several lines
marvin = Person(
      name='Marvin Arnold',
      gender='male',
      nationality='American',
      hometown='New Orleans',
      email='marvin@meet.mit.edu',
      hashed_password=hash_password('marvin'))
````

6. Change the imports in `hello.py` as required:
````python
from flask import Flask, render_template, redirect, url_for, request, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Person, Base
import hashlib
import initialize
## App setup
app = Flask(__name__)
# DANGER!! IN PRODUCTION, DO NOT INCLUDE INLINE PASSWORD
app.secret_key = 'super secret string'
## DB setup
engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()
````

## Enable sign in
1. Add password helper methods to `hello.py`:
````python
## Password helpers
# Use MD5 to hash a cleartext password
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
# Returns True if Person with email has password
def validate(email, password):
    query = dbSession.query(Person).filter(
        Person.email.in_([email]),
        Person.hashed_password.in_([hash_password(password)])
    )
    return query.first() != None
````
2. Create a `/secret` route in `hello.py` that only logged in users should be able to see:
````python
@app.route('/secret')
def secret():
    email = session.get('email')
    if not email:
        return redirect(url_for('signin'))
    else:
        return render_template('secret.html', email=email)
````

3. Create a template `templates/secret.html` to display the email of the logged in user.
````python
{% extends "base.html" %}
{% block content %}
  <div class="container">
    <h1>Hello {{email}}</h1>
  </div>
{% endblock %}
````
4. Add a route `/sigin` to `hello.py` to allow users to login:
````python
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None
    if request.method == 'POST':
        email = str(request.form['email'])
        password = str(request.form['password'])
        is_valid = validate(email, password)
        if is_valid == False:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['email'] = email
            return redirect(url_for('signin'))
    return render_template('signin.html', error=error)
````

5. Finally, add a corresponding template in `templates/signin.html`:
````python
{% extends "base.html" %}
{% block content %}
  <div class="container">
    {% if error %}
      <div class="alert alert-danger" role="alert">
        <strong>Oh snap!</strong> {{error}}
      </div>
    {% endif %}
    <form action="/signin" method="POST">
      <fieldset class="form-group">
        <label for="email">Email address</label>
        <input type="email" class="form-control" id="email" placeholder="Enter email" name='email' value="{{request.form.email }}">
        <small class="text-muted">We'll never share your email with anyone else.</small>
      </fieldset>
      <fieldset class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" placeholder="Password" name='password'>
      </fieldset>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
{% endblock %}
````
