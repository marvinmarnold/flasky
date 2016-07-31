from flask import Flask, render_template, redirect, url_for, request, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Person, Base, Photo, Tag
import hashlib

## App setup
app = Flask(__name__)
app.secret_key = 'super secret string'

## DB setup
engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()

## Fixtures
users = [
    {
        'name': "Marvin",
        'pic': "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.wildsoundmovies.com%2Fimages%2Fpulp_fiction_marvin.jpg&f=1",
        'description': "Normally, both your asses would be dead as fucking fried chicken, but you happen to pull this shit while I'm in a transitional period so I don't wanna kill you, I wanna help you."
    }
]

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

### Routes

@app.route('/')
def index():
    return render_template('index.html', users=users)

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
            user = dbSession.query(Person).filter_by(email=email).first()
            username = user.name
            if(username != None):
                print("Username found")
                session['name'] = username
                print(session['name'])
            return redirect(url_for('secret'))

    return render_template('signin.html', error=error)

@app.route('/secret')
def secret():
    email = session.get('email')
    if not email:
        return redirect(url_for('signin'))
    else:
        return render_template('secret.html', email=email)

@app.route('/user/<name>')
def user(name):
    user = dbSession.query(Person).filter_by(name=name).first()
    return render_template('user.html', user=user)

@app.route('/feed/<name>')
def feed(name):
    photos = dbSession.query(Photo).all()

    return render_template('feed.html', photos=photos)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
