from flask import Flask
from flask_socketio import SocketIO

CURRENT_BLOCK = 0
CURRENT_TX_ID = 0
NUMBER_OF_TX_IN_BLOCK = 0
BLOCK_THREAD_SLEEP = 3

ASYNC_MODE = None
THREAD_BLOCK = None
THREAD_TX = None

LATEST_FIVE_TASKS_URL = 'http://localhost:5002/tasks/latestfive'
LATEST_FIVE_BLOCKS_URL = 'http://blockexplorer.gamecredits.com/api/blocks/latest?limit=5'
LATEST_N_TX_URL = 'http://blockexplorer.gamecredits.com/api/transactions/latest?limit='

app = Flask(__name__)
socketio = SocketIO(app, async_mode=ASYNC_MODE)
