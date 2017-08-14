import unittest
import json

from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, Namespace

app = Flask(__name__)
socketio = SocketIO(app)
disconnected = None


@socketio.on('block_connected', namespace='/block')
def block_connected_test():
    emit('block_connected_message', 'Block Socket Connected Successfully!', namespace='/block')


@socketio.on('tx_connected', namespace='/tx')
def tx_connected_test():
    emit('tx_connected_message', 'Tx Socket Connected Successfully!', namespace='/tx')


@socketio.on('background_block_sender', namespace='/block')
def block_data_test():
    with open('block_structure.json') as data_file:
        data = json.load(data_file)
    emit('block_data', data, namespace='/block')


@socketio.on('background_tx_sender', namespace='/tx')
def tx_data_test():
    with open('tx_structure.json') as data_file:
        data = json.load(data_file)
    emit('tx_data', data, namespace='/tx')


@socketio.on('background_block_thread', namespace='/block')
def thread_block_data_test():
    array_of_blocks = []
    global current_block
    current_block = 0
    while True:
        del array_of_blocks[:]

        with open('block_data.json') as data_file:
            data = json.load(data_file)

        array_of_blocks.extend(data)
        difference_between_blocks = array_of_blocks[0]['height'] - current_block
        # print difference_between_blocks

        if difference_between_blocks > 0:
            current_block = array_of_blocks[0]['height']
            # print current_block
            emit('background_block_thread', current_block, namespace='/block')

        # socketio.sleep(3)
        break



class TestSocketIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_block_connection(self):
        client = socketio.test_client(app, namespace='/block')
        client.get_received('/block')
        client.emit('block_connected', namespace='/block')
        received = client.get_received('/block')
        expected_data = ['Block Socket Connected Successfully!']
        # print received
        self.assertEqual(received[0]['args'], expected_data)

    def test_tx_connection(self):
        client = socketio.test_client(app, namespace='/tx')
        client.get_received('/tx')
        client.emit('tx_connected', namespace='/tx')
        received = client.get_received('/tx')
        expected_data = ['Tx Socket Connected Successfully!']
        # print received
        self.assertEqual(received[0]['args'], expected_data)

    def test_block_data(self):
        client = socketio.test_client(app, namespace='/block')
        client.get_received('/block')
        client.emit('background_block_sender', namespace='/block')
        received = client.get_received('/block')
        extracted_block_data = received[0]['args'][0]
        # print received
        self.assertEqual(extracted_block_data['bits'], 'string')
        self.assertEqual(extracted_block_data['chainwork'], 'string')
        self.assertEqual(extracted_block_data['difficulty'], 'string')
        self.assertEqual(extracted_block_data['hash'], 'string')
        self.assertEqual(extracted_block_data['height'], 0)
        self.assertEqual(extracted_block_data['merkleroot'], 'string')
        self.assertEqual(extracted_block_data['nextblockhash'], 'string')
        self.assertEqual(extracted_block_data['nonce'], 0)
        self.assertEqual(extracted_block_data['previousblockhash'], 'string')
        self.assertEqual(extracted_block_data['size'], 0)
        self.assertEqual(extracted_block_data['target'], 'string')
        self.assertEqual(extracted_block_data['time'], 'string')
        self.assertEqual(extracted_block_data['total'], 0)

        self.assertEqual(extracted_block_data['tx'][0], 'string')

        self.assertEqual(extracted_block_data['version'], 0)
        self.assertEqual(extracted_block_data['work'], 0)

    def test_tx_data(self):
        client = socketio.test_client(app, namespace='/tx')
        client.get_received('/tx')
        client.emit('background_tx_sender', namespace='/tx')
        received = client.get_received('/tx')
        extracted_tx_data = received[0]['args'][0]
        # print received
        self.assertEqual(extracted_tx_data['blockhash'], 'string')
        self.assertEqual(extracted_tx_data['blocktime'], 0)
        self.assertEqual(extracted_tx_data['locktime'], 'string')
        self.assertEqual(extracted_tx_data['total'], 0)
        self.assertEqual(extracted_tx_data['txid'], 'string')
        self.assertEqual(extracted_tx_data['version'], 0)

        self.assertEqual(extracted_tx_data['vin'][0]['coinbase'], 'string')
        self.assertEqual(extracted_tx_data['vin'][0]['hex'], 'string')
        self.assertEqual(extracted_tx_data['vin'][0]['prev_txid'], 'string')
        self.assertEqual(extracted_tx_data['vin'][0]['sequence'], 0)
        self.assertEqual(extracted_tx_data['vin'][0]['txid'], 'string')
        self.assertEqual(extracted_tx_data['vin'][0]['vout_index'], 0)

        self.assertEqual(extracted_tx_data['vout'][0]['address'], 'string')
        self.assertEqual(extracted_tx_data['vout'][0]['asm'], 'string')
        self.assertEqual(extracted_tx_data['vout'][0]['index'], 0)
        self.assertEqual(extracted_tx_data['vout'][0]['reqSigs'], 0)
        self.assertTrue(extracted_tx_data['vout'][0]['spent'], True)
        self.assertEqual(extracted_tx_data['vout'][0]['txid'], 'string')
        self.assertEqual(extracted_tx_data['vout'][0]['type'], 'string')
        self.assertEqual(extracted_tx_data['vout'][0]['value'], 0)

    def test_thread_block_data(self):
        client = socketio.test_client(app, namespace='/block')
        client.get_received('/block')
        client.emit('background_block_thread', namespace='/block')
        received = client.get_received('/block')

        # print received


if __name__ == "__main__":
    unittest.main()
