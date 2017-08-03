# list = [1,6,2,2,3,6,7,10]
#
# i=0
# bol = True
# tmp = 0
# while i < len(list):
#     list[i]
#     #print(list[i])
#     if list[i] > tmp:
#         tmp=list[i]
#     print(tmp)
#     i+=1
#     if i == len(list):
#         break


# from flask import Flask, render_template, session, request, jsonify
# from flask_socketio import SocketIO, emit, join_room, leave_room, \
#     close_room, rooms, disconnect
# import requests as req
# import json
# #
# #
# def get_latest_block():
#     res = req.get('http://blockexplorer.gamecredits.com/api/blocks/latest?limit=1')
#     json_res = res.json()
#     block = json_res
#     return block
#
# print(len(get_latest_block()[0]['tx']))


# @app.route('/')
# def index():
#     root_dir = os.path.dirname(os.getcwd()) + '/PythonFlask-WebSocket-Server-master/angular-test'
#     print(root_dir)
#     return send_from_directory(os.path.join(root_dir, 'src'), 'index.html')
#
# @socketio.on('connection')
# def connection():
#     emit('msg', {'Radi....'})
#
#
# @socketio.on('connected', namespace='/test')
# def test_connect():
#     global thread
#     if thread is None:
#         thread = socketio.start_background_task(target=background_thread)
#     emit('msg', {'data': 'Connected'})
