import requests as req
import json
import config as conf

def get_latest_five_tasks():
    res = req.get(conf.LATEST_FIVE_TASKS_URL)
    five_tasks = res.json()
    return five_tasks

def get_latest_five_blocks():
    res = req.get(conf.LATEST_FIVE_BLOCKS_URL)
    five_blocks = res.json()
    return five_blocks

def get_latest_transactions(url):
    res = req.get(url)
    transactions = res.json()
    return transactions


# pronadji nacin kako da samo pozoves metode u thread-u u app.py
# glavni problem je trenutno sto ne moze da se odvoji socket iz app.py
# pronadji resenje za pozivanja socketa iz helpers.py
# def show_blocks_from_socket():
