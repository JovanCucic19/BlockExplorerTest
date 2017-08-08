import { Component } from '@angular/core';
import { SocketService } from './shared/socket.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [SocketService]
})

export class  AppComponent {

  title: string;
  private socket: any;
  odgovor: string;
  test: any;

  constructor(private socketService: SocketService){
    this.title = "Ovo je app componenta";
  }

  ngOnInit(): void {
    this.socket = this.socketService.initConnection();
    this.getInitMessage();
  }

  private getInitMessage(): void {
    this.socket = this.socketService.get().subscribe((odgovor) =>{
      this.test = odgovor
    });
  }

}
