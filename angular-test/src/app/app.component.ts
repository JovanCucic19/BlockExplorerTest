import { Component } from '@angular/core';
import {BlockSocketService, TxSocketService} from './shared/socket.service';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [BlockSocketService, TxSocketService]
})

export class  AppComponent {

  title: string;
  private socket: any;

  block_response: string;
  block_test: any;

  tx_response: string;
  tx_test: any;

  private blocks: any;
  block_data: any;

  private txs: any;
  tx_data: any;



  constructor(private blockSocketService: BlockSocketService, private txSocketService: TxSocketService){
    this.title = "Ovo je app componenta";
    this.blocks = [];
    this.txs = [];
  }

  ngOnInit(): void {
    this.socket = this.blockSocketService.initConnection();
    this.socket = this.txSocketService.initConnection();

    this.getBlockInitMessage();
    this.getTxInitMessage();

    this.getBlock();
    this.getTx();
  }

  private getBlockInitMessage(): void {
    this.socket = this.blockSocketService.getBlockConnection().subscribe((block_response) =>{
      this.block_test = block_response;
    });
  }

  private getTxInitMessage(): void {
    this.socket = this.txSocketService.getTxConnection().subscribe((tx_response) => {
      this.tx_test = tx_response;
    });
  }

  private getBlock(): void {
    this.socket = this.blockSocketService.getBlock().subscribe((block_data) =>{
      this.blocks.push(block_data);
    });
  }

  private getTx(): void {
    this.socket = this.txSocketService.getTx().subscribe((tx_data) =>{
      this.txs.push(tx_data);
    });
  }

}
