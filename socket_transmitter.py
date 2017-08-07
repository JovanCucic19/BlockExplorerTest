import helpers as helpp
import config as conf

conf.CURRENT_BLOCK = helpp.get_latest_five_blocks()[-1]['height']

def background_thread():
    niz_taskova = []
    while True:

        niz_blokova=[]
        del niz_blokova[:]
        niz_blokova.extend(helpp.get_latest_five_blocks())
        razlika = niz_blokova[0]['height']-conf.CURRENT_BLOCK

        if razlika != 0:
            conf.CURRENT_BLOCK=niz_blokova[0]['height']
            while razlika != 0:
                print("Trenutna broj tx u blokovima: {}".format(conf.BROJ_TX_U_BLOKOVIMA))

                conf.BROJ_TX_U_BLOKOVIMA += len(niz_blokova[-1+razlika]['tx'])
                conf.socketio.emit('background_block_sender', {'latest_block_data':niz_blokova[-1+razlika]}, namespace='/block')
                razlika-=1
                pass

        # print(conf.BROJ_TX_U_BLOKOVIMA)
        # return conf.BROJ_TX_U_BLOKOVIMA
        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)


def background_thread_tx():
    while True:
        print("Ovo je iz tx {}".format(conf.BROJ_TX_U_BLOKOVIMA))
        niz_tx=[]
        del niz_tx[:]

        if conf.BROJ_TX_U_BLOKOVIMA > 0:
            niz_tx.extend(helpp.get_latest_transactions(conf.LATEST_N_TX_URL+str(conf.BROJ_TX_U_BLOKOVIMA)))
            for tx in niz_tx:
                conf.socketio.emit('background_tx_sender', {'latest_tx_data':tx}, namespace='/tx')

            conf.BROJ_TX_U_BLOKOVIMA = 0
        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)
