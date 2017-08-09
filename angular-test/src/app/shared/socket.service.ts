import {Injectable} from '@angular/core';
import {Observable} from 'rxjs/Observable';

import * as socketio from 'socket.io-client';


let SERVER_URL = 'http://localhost:5004';
let block_namespace = '/block';
let tx_namespace = '/tx';

@Injectable()
export class BlockSocketService {

  private socket;

  constructor(){
    this.initSocket();
  }

  public initConnection(){
    this.socket.emit('block_connected');
  }


  private initSocket(): void {
    this.socket = socketio(SERVER_URL + block_namespace);
  }

  public getBlockConnection() {
    let observable = new Observable(observer => {
      this.socket.on('block_response', (data) =>{
        observer.next(data.block_data);
        console.log(data.block_data);
      });
      return () => {
        this.socket.disconnect();
      };
    });
    return observable;
  }

  public getBlock() {
    let observable = new Observable(observer => {
      this.socket.on('background_block_sender', (data) =>{
        observer.next(data.latest_block_data);
        console.log(data);
      });
      return () => {
        this.socket.disconnect();
      };
    });
    return observable;
  }

}

@Injectable()
export class TxSocketService {
  private socket;

  constructor(){
    this.initSocket();
  }

  public initConnection(){
    this.socket.emit('tx_connected');
  }

  private initSocket(): void {
    this.socket = socketio(SERVER_URL + tx_namespace);
  }

  public getTxConnection(){
    let observable = new Observable(observer => {
      this.socket.on('tx_response', (data) =>{
        observer.next(data.tx_data);
        console.log(data);
      });
      return () => {
        this.socket.disconnect();
      };
    });
    return observable;
  }

  public getTx(){
    let observable = new Observable(observer => {
      this.socket.on('background_tx_sender', (data) =>{
        observer.next(data.latest_tx_data);
        console.log(data);
      });
      return () => {
        this.socket.disconnect();
      };
    });
    return observable;
  }

}



