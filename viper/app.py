import os
import logging

from flask import Flask, request, jsonify

import viper

# Set logging level
logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s', level=logging.DEBUG)

# Create flask app
app = Flask(__name__)

# Create a SnakeCharmer object
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
def start() -> None:
    data = request.json
    game_id = data['game']['id']
    turn = data['turn']
    board = data['board']
    our_snake = data['you']

    logging.info('Received request to start new game with id {}'.format(game_id))
    snake_charmer.start_game(
        game_id=game_id,
        turn=turn,
        board=board,
        our_snake=our_snake
    )

    return 'Game started'


# To implement POST/move
@app.route('/move', methods=['POST'])
def move():
    raise NotImplementedError

# To implement POST/end
@app.route('/end', methods=['POST'])
def end():
    raise NotImplementedError
