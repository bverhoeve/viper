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
    viperDict = data['you']

    logging.info(f'Received request to start new game with id {game_id}')
    viper = snake_charmer.start_game(
        game_id=game_id,
        turn=turn,
        board=board,
        viperDict=viperDict
    )

    logging.info(
        f'Started game with id {game_id}. The generated viper is: {str(viper)}.'
    )
    print(viper.get_config())
    return jsonify(viper.get_config())


# To implement POST/move
@app.route('/move', methods=['POST'])
def move():
    return {
        move: "up",
        shout: "Brecht is een dikke miet."
    }

# To implement POST/end
@app.route('/end', methods=['POST'])
def end() -> None:
    data = request.json
    game_id = data['game']['id']
    logging.info(f'Received request to end game with id {game_id}.')
    snake_charmer.end_game(game_id)
    logging.info(
        f'Ended game with id {game_id}.' + 
        f'Number of games still running: {snake_charmer.get_numer_of_active_games()}.'
    )
