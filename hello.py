from flask import Flask, render_template
app = Flask(__name__)

users = [
    {
        'name': "Marvin",
        'pic': "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.wildsoundmovies.com%2Fimages%2Fpulp_fiction_marvin.jpg&f=1",
        'description': "Normally, both your asses would be dead as fucking fried chicken, but you happen to pull this shit while I'm in a transitional period so I don't wanna kill you, I wanna help you."
    }
]

@app.route('/')
def index():
  return render_template('index.html', users=users)

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)
