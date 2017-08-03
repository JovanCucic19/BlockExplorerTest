import { Component } from '@angular/core';

import { BlockService } from './block.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [BlockService],
  styleUrls: ['./app.component.css']
})

export class  AppComponent {
  message : Object;
  title: string;
  latestBlocks: any = [];

  constructor(private blockService : BlockService) {
    this.message = "nesto i neko"
    this.title = "Angular test projekat"
    console.log(this.message)
  }

  ngOnInit() {
    this.blockService
        .getMessage()
        .subscribe(data => {
          this.message = data,
          this.latestBlocks.push(data);
        });
  }
  sendMsg(message){
     this.blockService.sendMessage(this.message);
     console.log(this.message[0].height)
  }

}
