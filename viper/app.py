import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello from Viper!'

# To implement GET/ping
@app.route('/ping')
def ping():
  raise NotImplementedError

# To implement POST/start
@app.route('/start')
def start():
  raise NotImplementedError

# To implement POST/move
@app.route('/move')
def move():
  raise NotImplementedError

# To implement POST/end
@app.route('/end')
def end():
  raise NotImplementedError
