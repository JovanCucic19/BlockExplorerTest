from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests as req
import json
import os
import helpers as helpp
import config as conf
import logging
import socket_transmitter as st


# opcija za logovanje samo gresaka, iskljucivanje logovanja zahteva
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@conf.app.route('/')
def index():
    return render_template('index.html', async_mode=conf.socketio.async_mode)

@conf.socketio.on('block_connected', namespace='/block')
def block_connect():
    if conf.THREAD_BLOCK is None:
        conf.THREAD_BLOCK = conf.socketio.start_background_task(target=st.background_thread)
    emit('block_response', {'block_data': 'Block connected'})

@conf.socketio.on('tx_connected', namespace='/tx')
def tx_connect():
    if conf.THREAD_TX is None:
        conf.THREAD_TX = conf.socketio.start_background_task(target=st.background_thread_tx)
    emit('tx_response', {'tx_data': 'Tx connected'})


if __name__ == '__main__':
    conf.socketio.run(conf.app, debug=True, port=5004)
