import helpers as helpp
import config as conf

conf.CURRENT_BLOCK = helpp.get_latest_five_blocks()[-1]['height']

def block_buffer():
    array_of_blocks = []
    del array_of_blocks[:]
    array_of_blocks.extend(helpp.get_latest_five_blocks())
    return array_of_blocks


def first_block_from_buffer():
    block_height = block_buffer()[0]['height']
    return block_height


def emit_new_blocks():
    difference_between_blocks = first_block_from_buffer() - conf.CURRENT_BLOCK

    if difference_between_blocks > 0:
        conf.CURRENT_BLOCK = first_block_from_buffer()
        while difference_between_blocks > 0:
            print("Current number tx in block: {}".format(conf.NUMBER_OF_TX_IN_BLOCK))

            conf.NUMBER_OF_TX_IN_BLOCK += len(block_buffer()[-1 + difference_between_blocks]['tx'])
            conf.socketio.emit('background_block_sender',
                               {'latest_block_data': block_buffer()[-1 + difference_between_blocks]},
                               namespace='/block')
            difference_between_blocks -= 1
            pass


def block_background_thread():
    while True:
        emit_new_blocks()
        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)


def tx_buffer():
    array_of_tx = []
    del array_of_tx[:]
    array_of_tx.extend(helpp.get_latest_transactions(conf.LATEST_N_TX_URL + str(conf.NUMBER_OF_TX_IN_BLOCK)))
    return array_of_tx


def emit_new_tx():
    print("Info about tx's in block {}".format(conf.NUMBER_OF_TX_IN_BLOCK))

    if conf.NUMBER_OF_TX_IN_BLOCK > 0:
        tx_buffer()
        for tx in tx_buffer():
            conf.socketio.emit('background_tx_sender', {'latest_tx_data': tx}, namespace='/tx')

        conf.NUMBER_OF_TX_IN_BLOCK = 0


def tx_background_thread():
    while True:
        emit_new_tx()
        conf.socketio.sleep(conf.BLOCK_THREAD_SLEEP)
