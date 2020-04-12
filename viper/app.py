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

if __name__ == '__main__':
  if os.environ['ENV'] == 'production':
    port = 80
  else:
    port = 5000
  
  app.run(host='0.0.0.0', port=port)

