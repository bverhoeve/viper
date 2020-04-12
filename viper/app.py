import os
import viper
from flask import Flask, request, jsonify

app = Flask(__name__)
snake_charmer = viper.SnakeCharmer()

@app.route('/')
def hello():
  return 'Viper is alive and ready to battle!'

# To implement GET/ping
@app.route('/ping')
def ping():
  return 'Pong'

# To implement POST/start
@app.route('/start', methods=['POST'])
def start():
  data = request.json
  print('Game start')


# To implement POST/move
@app.route('/move', methods=['POST'])
def move():
  raise NotImplementedError

# To implement POST/end
@app.route('/end', methods=['POST'])
def end():
  raise NotImplementedError
