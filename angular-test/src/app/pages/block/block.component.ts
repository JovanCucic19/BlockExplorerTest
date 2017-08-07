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
    this.title = "Angular test projekat"
    // console.log(this.message)
    // console.log("Evo me iz konstruktora")
  }

  ngOnInit() {

    this.blockService.getMsg()
    this.blockService
        .getMessage()
        .subscribe(data => {
          this.message = data,
          this.latestBlocks.push(data);
        });
        //console.log(this.blockService.getMsg());

      // console.log(this.latestBlocks)
  }

}
