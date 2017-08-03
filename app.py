from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import requests as req
import json
import os
import config as conf
import logging


# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
# opcija za logovanje samo gresaka, iskljucivanje logovanja zahteva
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def get_latest_block():
    res = req.get(conf.LATEST_BLOCK_URL)
    block = res.json()
    return block

def get_latest_five():
    res = req.get(conf.LATEST_FIVE_BLOCKS_URL)
    five_tasks = res.json()
    return five_tasks

def background_thread():
    niz_taskova = []
    while True:
        del niz_taskova[:]
        niz_taskova.extend(get_latest_five())
        razlika = niz_taskova[-1]['id']-conf.CURRENT_BLOCK

        if razlika != 0:
            conf.CURRENT_BLOCK=niz_taskova[-1]['id']
            while razlika != 0:
                print("Trenutna razlika je: {}".format(razlika))
                socketio.emit('message', {'data':niz_taskova[len(niz_taskova)-razlika]}, namespace='/test')
                razlika-=1
                pass

        print('Nema razlike trenutno')
        # print("Duzina niza je {}".format(len(niz_taskova[0])))
        # print(test_niz.id)

        socketio.sleep(conf.BLOCK_THREAD_SLEEP)

        #conf.CURRENT_BLOCK = get_latest_block()[0]['height']

@app.route('/')
def index():
    # root_dir = os.path.dirname(os.getcwd()) + '/PythonFlask-WebSocket-Server-master/angular-test'
    # print(root_dir)
    # return send_from_directory(os.path.join(root_dir, 'src'), 'index.html')
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('connected', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected'})


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5004)
