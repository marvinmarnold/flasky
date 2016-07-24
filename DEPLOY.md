# Deploy a Flask project to Heroku
## **Make sure you are using venv**

These instructions are summarized from the [official guide](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).
1. Create an account at `heroku.com`
2. Install setuptools, `pip3.5 install setuptools`
3. Install Ruby, `sudo apt-get install ruby`
4. Install Heroku CLI, `wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh`
5. Login to the CLI:
```bash
$ heroku login
> Enter your Heroku credentials.
> Email: python@example.com
> Password:
```
6. Run the following:
````
$ heroku create --buildpack heroku/python
# Copy requirements.txt to the root of your project
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open
````
