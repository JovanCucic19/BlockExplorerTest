import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { SocketIoModule } from 'ng-socket-io';
import { SocketIoConfig } from 'ng-socket-io';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';


//const config: SocketIoConfig = { url: 'http://localhost:5004/block', options: {} };

const appRoutes: Routes = []

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
