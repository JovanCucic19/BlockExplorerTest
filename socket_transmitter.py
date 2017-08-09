import helpers as helpp
import config as conf

conf.CURRENT_BLOCK = helpp.get_latest_five_blocks()[0]['height']


def background_thread():
    while True:

        array_of_blocks = []
        del array_of_blocks[:]
        array_of_blocks.extend(helpp.get_latest_five_blocks())
        difference_between_blocks = array_of_blocks[0]['height']-conf.CURRENT_BLOCK

        if difference_between_blocks != 0:
            conf.CURRENT_BLOCK=array_of_blocks[0]['height']
            while difference_between_blocks != 0:
                print("Trenutna broj tx u blokovima: {}".format(conf.BROJ_TX_U_BLOKOVIMA))

                conf.BROJ_TX_U_BLOKOVIMA += len(array_of_blocks[-1+difference_between_blocks]['tx'])
                conf.socketio.emit('background_block_sender', 
                                   {'latest_block_data': array_of_blocks[ -1 + difference_between_blocks]},
                                   namespace='/block')
                difference_between_blocks -= 1
                pass

        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)


def background_thread_tx():
    while True:
        print("Ovo je iz tx {}".format(conf.BROJ_TX_U_BLOKOVIMA))
        array_of_tx = []
        del array_of_tx[:]

        if conf.BROJ_TX_U_BLOKOVIMA > 0:
            array_of_tx.extend(helpp.get_latest_transactions(conf.LATEST_N_TX_URL + str(conf.BROJ_TX_U_BLOKOVIMA)))
            for tx in array_of_tx:
                conf.socketio.emit('background_tx_sender', {'latest_tx_data': tx}, namespace='/tx')

            conf.BROJ_TX_U_BLOKOVIMA = 0
        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)
