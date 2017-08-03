import { Component } from '@angular/core';

import { HomeService } from './home.service';

@Component({
  selector: 'exploder-home',
  templateUrl: 'home.component.html'
})

export class HomeComponent{
  home:string;

  constructor(private homeService : HomeService) {
    this.home = "Ovo je home deo"
  }

  ngOnInit() {

  }

}
