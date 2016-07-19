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

1. Create `hello.py` (Sublime, etc.)
2. Go back to terminal with `(venv)` and run `python hello.py`.
3. Open up your browser (Firefox, etc.) and type in the address `localhost:5000` or `127.0.0.1:5000`.
4. You should see **Hello World!**
