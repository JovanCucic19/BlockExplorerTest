import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable'
import 'rxjs/add/operator/map';
import { Socket } from 'ng-socket-io';

@Injectable()
export class BlockService {

  nasaData: Object;
  private nasSocket;

  constructor(private socket: Socket){}

  getMessage(){
    return this.socket
          .fromEvent<any>("message")
          .map(data => data);
  }

  public getMsg(){
    this.socket.on('message', (data) =>{

      // return data.data;
      console.log(data.data.height);
    });
  }

}
