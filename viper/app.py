import socket
import logging

from flask import Flask, request, jsonify

import viper

# Set logging level
hostname: str = socket.gethostname()
logfile_name: str = hostname + '.log'
logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s', level=logging.DEBUG)

# Create flask app
app = Flask(__name__)

# Create a SnakeCharmer object
snake_charmer = viper.SnakeCharmer()

@app.route('/')
def hello():
    return 'Viper is alive and ready to battle!'

# To implement GET/ping
@app.route('/ping', methods=['GET', 'POST'])
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
    return jsonify(viper.get_config())


# To implement POST/move
@app.route('/move', methods=['POST'])
def move():
    data = request.json
    game_id = data['game']['id']
    turn = data['turn']
    board = data['board']
    viperDict = data['you']

    logging.info(f'Received move request for game with id {game_id}')
    
    return jsonify(snake_charmer.move(
        game_id=game_id,
        turn=turn,
        board=board,
        viperDict=viperDict
    ))
    

# To implement POST/end
@app.route('/end', methods=['POST'])
def end() -> None:
    data = request.json
    game_id = data['game']['id']
    logging.info(f'Received request to end game with id {game_id}.')
    snake_charmer.end_game(game_id)
    logging.info(
        f'Ended game with id {game_id}.'
    )
    return ''
