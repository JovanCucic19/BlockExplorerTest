import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { SocketIoModule } from 'ng-socket-io';
import { SocketIoConfig } from 'ng-socket-io';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { BlockComponent } from './pages/block/block.component';
import { HomeComponent } from './pages/home/home.component';

import { BlockService } from './pages/block/block.service';
import { HomeService } from './pages/home/home.service';

const config: SocketIoConfig = { url: 'http://localhost:5004/test', options: {} };

const appRoutes: Routes = [
    {path: 'blocks', component: BlockComponent},
    {path: 'home', component: HomeComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    BlockComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    SocketIoModule.forRoot(config),
    RouterModule.forRoot(appRoutes)
  ],
  providers: [
    BlockService,
    HomeService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
