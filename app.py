from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import requests as req
import json
import os
import helpers as helpp
import config as conf
import logging


app = Flask(__name__)
socketio = SocketIO(app, async_mode=conf.ASYNC_MODE)
# socketio_tx = SocketIO(app, async_mode=conf.ASYNC_MODE)
# opcija za logovanje samo gresaka, iskljucivanje logovanja zahteva
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

conf.CURRENT_BLOCK = helpp.get_latest_five_blocks()[-1]['height']

def background_thread():
    niz_taskova = []
    while True:

        # ==== OVO JE TEST ZA REST SERVER NE BRISI ====

        # del niz_taskova[:]
        # niz_taskova.extend(get_latest_five_tasks())
        # razlika = niz_taskova[-1]['id']-conf.CURRENT_BLOCK
        #
        # if razlika != 0:
        #     conf.CURRENT_BLOCK=niz_taskova[-1]['id']
        #     while razlika != 0:
        #         # print("Trenutna razlika je: {}".format(razlika))
        #         socketio.emit('message', {'data':niz_taskova[len(niz_taskova)-razlika]}, namespace='/test')
        #         razlika-=1
        #         pass

        # print('Nema razlike trenutno')

        # ==== OVDE SE ZAVRSAVA TEST ZA REST SEVER ====

        niz_blokova=[]
        del niz_blokova[:]
        niz_blokova.extend(helpp.get_latest_five_blocks())
        razlika = niz_blokova[0]['height']-conf.CURRENT_BLOCK
        # print("Ispisacu {} blokova".format(razlika))
        # print(len(niz_blokova[0]['tx']))


        if razlika != 0:
            conf.CURRENT_BLOCK=niz_blokova[0]['height']
            while razlika != 0:
                print("Trenutna broj tx u blokovima: {}".format(conf.BROJ_TX_U_BLOKOVIMA))

                conf.BROJ_TX_U_BLOKOVIMA += len(niz_blokova[-1+razlika]['tx'])
                socketio.emit('background_block_sender', {'latest_block_data':niz_blokova[-1+razlika]}, namespace='/block')
                razlika-=1
                pass

        # print(conf.BROJ_TX_U_BLOKOVIMA)
        # return conf.BROJ_TX_U_BLOKOVIMA


        # Rasclaniti conf.BROJ_TX_U_BLOKOVIMA da bi mogle dve metode da se razdvoje kako bi se
        # dobila veca modularnost, debatovati o potrebi modularnosti
        # niz_tx=[]
        # del niz_tx[:]
        # niz_tx.extend(helpp.get_latest_transactions(conf.LATEST_N_TX_URL+str(conf.BROJ_TX_U_BLOKOVIMA)))
        #
        # if conf.BROJ_TX_U_BLOKOVIMA != 0:
        #     for tx in niz_tx:
        #         socketio.emit('message', {'data':tx}, namespace='/tx')
        #         print(tx['txid'])
        #     conf.BROJ_TX_U_BLOKOVIMA = 0

        # print()
        # print("Duzina niza {}".format(len(niz_tx)))
        # socketio.emit('message', {'data':"nesto"}, namespace='/block')
        socketio.sleep(conf.BLOCK_THREAD_SLEEP)


def background_thread_tx():
    while True:
        # socketio.sleep(1)
        print("Ovo je iz tx {}".format(conf.BROJ_TX_U_BLOKOVIMA))
        niz_tx=[]
        del niz_tx[:]

        if conf.BROJ_TX_U_BLOKOVIMA > 0:
            niz_tx.extend(helpp.get_latest_transactions(conf.LATEST_N_TX_URL+str(conf.BROJ_TX_U_BLOKOVIMA)))
            for tx in niz_tx:
                socketio.emit('background_tx_sender', {'latest_tx_data':tx}, namespace='/tx')
            
            conf.BROJ_TX_U_BLOKOVIMA = 0

        # print()
        # print("Duzina niza {}".format(len(niz_tx)))
        # socketio.emit('message', {'data':"nesto"}, namespace='/block')
        socketio.sleep(conf.BLOCK_THREAD_SLEEP)


# def background_thread():
#     niz_taskova = []
#     while True:
#
#         # ==== OVO JE TEST ZA REST SERVER NE BRISI ====
#
#         # del niz_taskova[:]
#         # niz_taskova.extend(get_latest_five_tasks())
#         # razlika = niz_taskova[-1]['id']-conf.CURRENT_BLOCK
#         #
#         # if razlika != 0:
#         #     conf.CURRENT_BLOCK=niz_taskova[-1]['id']
#         #     while razlika != 0:
#         #         # print("Trenutna razlika je: {}".format(razlika))
#         #         socketio.emit('message', {'data':niz_taskova[len(niz_taskova)-razlika]}, namespace='/test')
#         #         razlika-=1
#         #         pass
#
#         # print('Nema razlike trenutno')
#
#         # ==== OVDE SE ZAVRSAVA TEST ZA REST SEVER ====
#
#         niz_blokova=[]
#         del niz_blokova[:]
#         niz_blokova.extend(helpp.get_latest_five_blocks())
#         razlika = niz_blokova[0]['height']-conf.CURRENT_BLOCK
#         # print("Ispisacu {} blokova".format(razlika))
#         # print(len(niz_blokova[0]['tx']))
#
#
#         if razlika != 0:
#             conf.CURRENT_BLOCK=niz_blokova[0]['height']
#             while razlika != 0:
#                 # print("Trenutna razlika je: {}".format(razlika))
#                 conf.BROJ_TX_U_BLOKOVIMA += len(niz_blokova[-1+razlika]['tx'])
#                 socketio.emit('message', {'data':niz_blokova[-1+razlika]}, namespace='/block')
#                 razlika-=1
#                 pass
#
#         print(conf.BROJ_TX_U_BLOKOVIMA)
#
#
#         # Rasclaniti conf.BROJ_TX_U_BLOKOVIMA da bi mogle dve metode da se razdvoje kako bi se
#         # dobila veca modularnost, debatovati o potrebi modularnosti
#         niz_tx=[]
#         del niz_tx[:]
#         niz_tx.extend(helpp.get_latest_transactions(conf.LATEST_N_TX_URL+str(conf.BROJ_TX_U_BLOKOVIMA)))
#
#         if conf.BROJ_TX_U_BLOKOVIMA != 0:
#             for tx in niz_tx:
#                 socketio.emit('message', {'data':tx}, namespace='/tx')
#                 print(tx['txid'])
#             conf.BROJ_TX_U_BLOKOVIMA = 0
#
#         # print()
#         # print("Duzina niza {}".format(len(niz_tx)))
#         # socketio.emit('message', {'data':"nesto"}, namespace='/block')
#         socketio.sleep(conf.BLOCK_THREAD_SLEEP)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('block_connected', namespace='/block')
def block_connect():
    if conf.THREAD_BLOCK is None:
        conf.THREAD_BLOCK = socketio.start_background_task(target=background_thread)
    emit('block_response', {'block_data': 'Block connected'})

@socketio.on('tx_connected', namespace='/tx')
def tx_connect():
    if conf.THREAD_TX is None:
        conf.THREAD_TX = socketio.start_background_task(target=background_thread_tx)
    emit('tx_response', {'tx_data': 'Tx connected'})


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5004)
