import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable'
import 'rxjs/add/operator/map';
import { Socket } from 'ng-socket-io';

@Injectable()
export class BlockService {

    constructor(private socket: Socket) {}

    getMessage() {
        return this.socket
            .fromEvent<any>("message")
            .map(data => data.data);
    }

    sendMessage(message: Object) {
      this.socket.emit("message", message);
    //  console.log()
    }
}
