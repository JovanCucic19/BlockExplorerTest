from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests as req
import json
import os
import helpers as helpp
import config as conf
import initiated_values as iv
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
    if iv.THREAD_BLOCK is None:
        iv.THREAD_BLOCK = conf.socketio.start_background_task(target=st.block_background_thread)
    emit('block_response', {'block_data': 'Block connected'})
    print("Block socket is connected")


@conf.socketio.on('disconnect', namespace='/block')
def test_client_block_disconnect():
    print('Client disconnected from block socket')


@conf.socketio.on('disconnect', namespace='/tx')
def test_client_tx_disconnect():
    print('Client disconnected from tx socket')


@conf.socketio.on('tx_connected', namespace='/tx')
def tx_connect():
    if iv.THREAD_TX is None:
        iv.THREAD_TX = conf.socketio.start_background_task(target=st.tx_background_thread)
    emit('tx_response', {'tx_data': 'Tx connected'})
    print("Tx socket is connected")


if __name__ == '__main__':
    conf.socketio.run(conf.app, debug=False, port=5004)
