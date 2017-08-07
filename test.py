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
