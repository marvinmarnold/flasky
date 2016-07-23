# Flasky
Sample app for MEET 2016 Y3 to practice with Flask.

## Exercise 0: Setup
Go to github.com and create an account. Create a new PUBLIC repository named `flasky`. Do not add a README.


```bash
# Verify directory structure
$ cd && pwd
> /home/student # if it doesn’t say that, get an instructor
$ mkdir flasky && cd flasky


# Ignore if done previously - setup venv
$ sudo apt-get install -y python3-venv # ignore if done previously
$ pip3.5 install --upgrade pip

# Use venv to setup Flask
$ python3.5 -m venv venv
$ source venv/bin/activate
$ pip3.5 install flask

# Ignore if done previously: configure git --global
$ git config --global user.email “you@meet.mit.edu”
$ git config --global user.name “First Last”

$ git init
$ echo 'venv' > .gitignore # add venv folder to .gitignore

$ git remote add origin https://github.com/YOUR_USERNAME/flasky.git
$ git add . # stage all files
$ git commit -m “My first commit”
$ git push origin master
```

## Exercise 1: Simple Hello World!

- Create `hello.py` (Sublime, etc.). Add:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

if __name__ == '__main__':
  app.run(debug=True)
```
- Go back to terminal with `(venv)` and run `python hello.py`.
- Open up your browser (Firefox, etc.) and type in the address `localhost:5000` or `127.0.0.1:5000`.
- You should see **Hello World!**

## Exercise 2: Simple Hello World with dynamic route
- Modify `hello.py` to:

```python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
  return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
  app.run(debug=True)
```
- Go to `localhost:5000/user/YOUR_NAME` and confirm it outputs **Hello, YOUR_NAME!**.

### Exercise 3: Templates

#### Exercise 3a: Referencing Templates
In `hello.py`, add `render_template` to imports and have methods call `render_template` instead of returning HTML directly.

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)

if __name__ == '__main__':
  app.run(debug=True)
```

#### Excercise 3b: Creating Templates
- Create a directory `/templates` (relative to project root, not computer root)
- Create `/templates/index.html` containing `<h1>Hello World!</h1>`.
- Create `/templates/user.html` containing `<h1>Hello, {{name}}!</h1>`.
- If not still running, restart server with `python hello.py`
- Go to `localhost:5000` and `localhost:5000/YOU` and make sure pages still load.

### Exercise 4: Custom Error Pages
- Add a custom 404 route to `hello.py` with:

```python
...

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),  404

if __name__ == '__main__':
  app.run(debug=True)
```
- Create a file `/templates/404.html` with the content `<h1>Sorry, this page was not found.</h1>`
- Confirm that `localhost:5000/some-non-existant-route` loads the new 404 page.

### Excercise 5: Templates
#### Excercise 5a: User template blocks
- Add a title, navbar, and content blocks to `user.html`.

```python
{% block title %}Flasky{% endblock %}

{% block navbar %}
  <ul>
    <li><a href='/'>Home</a></li>
  </ul>
{% endblock %}

{% block content %}
  <h1>Hello, {{name}}!</h1>
{% endblock %}
```

- Open `localhost:5000/user/name` and make sure it loads.

#### Excercise 5b: Create base template
- Create 'templates/base.html':

```python
{% block title %}Flasky{% endblock %}

{% block navbar %}
  <ul>
    <li><a href='/'>Home</a></li>
  </ul>
{% endblock %}

{% block content %}
  <h1>Hello, {{name}}!</h1>
{% endblock %}
```
- Have `user.html`, `index.html`, and `404.html` all appropriately extend `base.thml`.

```python
# user.html
{% block content %}
  <h1>Hello, {{name}}!</h1>
{% endblock %}

# index.html
{% extends "base.html" %}

{% block content %}
  <h1>Hello World!</h1>
{% endblock %}

# 404.html
{% extends "base.html" %}

{% block content %}
  <h1>Sorry, this page was not found.</h1>
{% endblock %}

```

- Verify that all pages now load with a navbar: `localhost:5000`, `localhost:5000/yourname` &
 `localhost:5000/user/yourname`.


### Databases

#### Refresher Exercises  Setup
- Install Flask wrapper for SQLAlchemy
```bash
# Verify directory structure
$ cd && pwd
> /home/student # if it doesn’t say that, get an instructor
$ cd flasky
$ pip3.5 install flask-sqlalchemy
```

Now, set up the database. *Warning: if you already have people in the
database, this command will delete all of them and reset it to Marvin,
Lorenzo, Anna, Lisa, and Eric.* You can use this any time if you mess up the
database or add too many people.

    python initialize.py

For this lab, you'll write your code either interactively in Python, or in
`add_to_database.py`.

#### Exercise: Create
Write code in `add_to_database.py` to add you and your partner to the database.
Run your code and use `print_databases.py`

#### Exercise: Read

1. In Python, use `session.query` to find the hometown of the only German person in the database.

2. Write a function `find_nationality` in `add_to_database.py` that takes a
   nationality and returns a list of names of people in the database with that
   nationality. For example, `find_nationality('American')` should return
   `['Eric Westberg', 'Lorenzo Brown', 'Marvin Arnold, 'Anna Premo']` (the order doesn't matter). Your code
   should start like this:

    def find_nationality(nat):

#### Exercise: Update
1. Suppose Lorenzo changes his first name to Lori. Update his name in the
   database, and use both `print_databases.py` and `session.query` to make sure
   your change worked.

2. Do the same thing if Lisa changes her first name to Anastasia.

#### Exercise: Delete
From Python, remove all the instructors and staff from the database so that only students
and TAs are left.

#### Integrate SQLAlchemy into your Project!

1. Copy the files to your project app
2. Rename the database in initialize.py, add_to_database.py, print_databases.py
3. Update database.setup.py with your Models
4. Update initialize.py to populate your tables
5. Test adding new data in add_to_database.py
6. Initialize and test with print_databases.py
7. Integrate into your app (hint: use add_to_database.py as reference)






