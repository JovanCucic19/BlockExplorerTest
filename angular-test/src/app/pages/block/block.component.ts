import { Component } from '@angular/core';

import { BlockService } from './block.service';

@Component({
  selector: 'exploder-block',
  templateUrl: 'block.component.html'
})

export class BlockComponent{
  message: Object;
  title: string;
  latestBlocks: any=[];

  constructor(private blockService : BlockService) {
    this.message = "nesto i neko"
    this.title = "Angular test projekat"
    // console.log(this.message)
    console.log("Evo me iz konstruktora")
  }

  ngOnInit() {
    this.blockService
        .getMessage()
        .subscribe(data => {
          this.message = data,
          this.latestBlocks.push(data);
        });
      console.log(this.latestBlocks[0])
  }
  sendMsg(message){
     this.blockService.sendMessage(this.message);
     console.log(this.message[0])
     console.log("Evo me iz sendMsg")
  }

}
