import {Injectable} from '@angular/core';
import {Observable} from 'rxjs/Observable';

import * as socketio from 'socket.io-client';


let SERVER_URL = 'http://localhost:5004/block';

@Injectable()
export class SocketService {

  private socket;

  constructor(){
    this.initSocket();
  }

  public initConnection(){
    this.socket.emit('block_connected');
  }

  private initSocket(): void {
    this.socket = socketio(SERVER_URL);
  }

  public get() {
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

}
