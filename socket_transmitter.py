import helpers as helpp
import config as conf


conf.CURRENT_BLOCK = helpp.get_latest_five_blocks()[-1]['height']


def background_thread():
    while True:
        array_of_blocks = []
        del array_of_blocks[:]
        array_of_blocks.extend(helpp.get_latest_five_blocks())
        difference_between_blocks = array_of_blocks[0]['height'] - conf.CURRENT_BLOCK

        if difference_between_blocks > 0:
            conf.CURRENT_BLOCK = array_of_blocks[0]['height']
            while difference_between_blocks > 0:
                print("Trenutna broj tx u blokovima: {}".format(conf.NUMBER_OF_TX_IN_BLOCK))

                conf.NUMBER_OF_TX_IN_BLOCK += len(array_of_blocks[-1 + difference_between_blocks]['tx'])
                conf.socketio.emit('background_block_sender', 
                                   {'latest_block_data': array_of_blocks[-1 + difference_between_blocks]},
                                   namespace='/block')
                difference_between_blocks -= 1
                pass

        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)


def background_thread_tx():
    while True:
        print("Ovo je iz tx {}".format(conf.NUMBER_OF_TX_IN_BLOCK))
        array_of_tx = []
        del array_of_tx[:]

        if conf.NUMBER_OF_TX_IN_BLOCK > 0:
            array_of_tx.extend(helpp.get_latest_transactions(conf.LATEST_N_TX_URL + str(conf.NUMBER_OF_TX_IN_BLOCK)))
            for tx in array_of_tx:
                conf.socketio.emit('background_tx_sender', {'latest_tx_data': tx}, namespace='/tx')

            conf.NUMBER_OF_TX_IN_BLOCK = 0
        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)
