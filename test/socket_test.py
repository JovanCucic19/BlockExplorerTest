import unittest
import json
import requests

from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, Namespace
from mock import mock, patch

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


@socketio.on('background_mock_block_sender', namespace='/block')
def block_mock_data_test():
    mock_block_data = {
        "bits": "0x1b05c193",
        "chainwork": "0x65bb3334c246beee",
        "difficulty": "11385.21547576",
        "hash": "db52e9d94210b0dbd22cca213275f0599c3a4c580ac9014b07fdd5b208779fd8",
        "height": 1750461,
        "merkleroot": "86feb4073bab1e9114a26baf0ec2aedd569e1fd86d7f3417ef45996d3de879c5",
        "nextblockhash": None,
        "nonce": 3047044099,
        "previousblockhash": "3c972dce5207d0aca93de092b7f69340b5f3053ce4879818e16e12a38f55d35e",
        "size": 1402,
        "target": "0x5c193000000000000000000000000000000000000000000000000L",
        "time": 1502881366,
        "total": "366.34138225",
        "tx": [
            "22b96e889dc272c307adf4878bb60e481fffcd4708be20598f72e486444536ee",
            "acceba9c589e9500b62376308c79d8e467d6a79601b5b1c4ac3e2da082d4fe11",
            "bf57bb76e08cdb62745aa99a9c6a34310422aadec03e9e6aee8083352d8d8c24",
            "96e249771366fa23ad332515130811aafb996ddc1d6a25c4f4bb30d0b361c525",
            "7bf516d3d3de2df073da9dddfb9aeca0840016b5ca26cde96c9209e5068c1203"
        ],
        "version": 2,
        "work": 48899874279188
    }
    emit('block_mock_data', mock_block_data, namespace='/block')

@socketio.on('background_mock_tx_sender', namespace='/tx')
def tx_mock_data_test():
    mock_tx_data = {
    "blockhash": "23c034d50ed039e22ac276652f788f237c98f3a028acc60288e0a1624b0d54b4",
    "blocktime": 1502888665,
    "locktime": 0,
    "total": 12.5001,
    "txid": "66b80940be43ff0aec5df5716c91257120b29354d70a58e07872eda1fa038b89",
    "version": 1,
    "vin": [
      {
        "coinbase": "0311b61a062f503253482f04d7429459080000002524000000352f737a62706f6f6c2ffabe6d6d6568d84c3da40e4816bd3dac64bf316e89f3d973126fc34fae0c022400a8fe180800000000000000",
        "hex": None,
        "prev_txid": None,
        "sequence": 0,
        "vout_index": None
      }
    ],
    "vout": [
      {
        "addresses": [
          "GfVRuK6D4EvAG9KoxVhBEV6xwT6451Dwab"
        ],
        "asm": "OP_DUP OP_HASH160 ed72a54b8926cb13d522e186c884dbd5c45998b1 OP_EQUALVERIFY OP_CHECKSIG",
        "reqSigs": 1,
        "spent": False,
        "type": "pubkeyhash",
        "value": 12.5001
      }
    ]
    }
    emit('tx_mock_data', mock_tx_data, namespace='/tx')


def get_data_from_url(url):
    response = requests.get(url)
    return response


def check_typeof_parameter(parameter):
    if isinstance(parameter, (int, float)):
        return parameter
    elif isinstance(parameter, str):
        return parameter
    elif parameter is None:
        return parameter
    else:
        raise ValueError('Invalid input')


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


    def test_mock_block_data(self):
        with mock.patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = mock.Mock()

            client = socketio.test_client(app, namespace='/block')
            client.get_received('/block')
            client.emit('background_mock_block_sender', namespace='/block')
            received = client.get_received('/block')

            mock_response.status_code = 200
            mock_response.content = received[0]['args'][0]

            response = get_data_from_url('http://blockexplorer.gamecredits.com/api/blocks/latest?limit=1')

            mock_hash = response.content['hash']
            mock_height = response.content['height']
            mock_nextblockhash = response.content['nextblockhash']

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content['hash'], check_typeof_parameter(mock_hash))
            self.assertEqual(response.content['height'], check_typeof_parameter(mock_height))
            self.assertEqual(response.content['nextblockhash'],
                             check_typeof_parameter(mock_nextblockhash))

    def test_mock_tx_data(self):
        with mock.patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = mock.Mock()

            client = socketio.test_client(app, namespace='/tx')
            client.get_received('/tx')
            client.emit('background_mock_tx_sender', namespace='/tx')
            received = client.get_received('/tx')

            mock_response.status_code = 200
            mock_response.content = received[0]['args'][0]

            response = get_data_from_url('http://blockexplorer.gamecredits.com/api/transactions/latest?limit=1')


            mock_blockhash = response.content['blockhash']
            mock_txid = response.content['txid']
            mock_total = response.content['total']

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content['blockhash'], check_typeof_parameter(mock_blockhash))
            self.assertEqual(response.content['txid'], check_typeof_parameter(mock_txid))
            self.assertEqual(response.content['total'], check_typeof_parameter(mock_total))



if __name__ == "__main__":
    unittest.main()
