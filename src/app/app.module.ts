import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {BrowserAnimationsModule, NoopAnimationsModule} from '@angular/platform-browser/animations'
import {RouterModule, Routes} from '@angular/router'
import {HttpClientModule} from '@angular/common/http'
import { MatButtonModule } from '@angular/material/button'
import {
  MatButtonToggleModule,
} from '@angular/material/button-toggle'

import {
  MatCardModule,
} from '@angular/material/card'

import {
  MatCheckboxModule,
} from '@angular/material/checkbox'

import {
  MatChipsModule,
} from '@angular/material/chips'

import {
  MatNativeDateModule,
  MatOptionModule,
} from '@angular/material/core'

import {
  MatDatepickerModule
} from '@angular/material/datepicker'

import {
  MatDialogModule
} from '@angular/material/dialog'

import {
  MatFormFieldModule,
} from '@angular/material/form-field'

import {
  MatGridListModule
} from '@angular/material/grid-list'

import {
  MatIconModule
} from '@angular/material/icon'

import {
  MatInputModule
} from '@angular/material/input'

import {
  MatListModule
} from '@angular/material/list'

import {
  MatProgressBarModule
} from '@angular/material/progress-bar'

import {
  MatProgressSpinnerModule
} from '@angular/material/progress-spinner'

import {
  MatRadioModule
} from '@angular/material/radio'

import {
  MatSelectModule
} from '@angular/material/select'

import {
  MatSidenavModule
} from '@angular/material/sidenav'

import {
  MatSlideToggleModule
} from '@angular/material/slide-toggle'

import {
  MatSliderModule
} from '@angular/material/slider'

import {
  MatSnackBarModule
} from '@angular/material/snack-bar'

import {
  MatStepperModule
} from '@angular/material/stepper'

import {
  MatTableModule
} from '@angular/material/table'

import {
  MatTabsModule
} from '@angular/material/tabs'

import {
  MatTooltipModule
} from '@angular/material/tooltip'

import {
  MatExpansionModule
} from '@angular/material/expansion';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { EventListComponent } from './components/event-list/event-list.component';
import {DatePipe} from './pipes/date.pipe';
import { PlanComponent } from './components/plan/plan.component'



const appRoutes: Routes = [
  {path: '', component: DashboardComponent},
]

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    EventListComponent,
    DatePipe,
    PlanComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserModule,
    NoopAnimationsModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCheckboxModule,
    MatFormFieldModule,
    MatSelectModule,
    MatInputModule,
    MatOptionModule,
    MatCardModule,
    MatDatepickerModule,
    MatNativeDateModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatExpansionModule,
    MatTooltipModule,
    MatProgressSpinnerModule,
    MatProgressBarModule,
    MatGridListModule,
    MatListModule,
    MatSlideToggleModule,
    MatSidenavModule,
    MatStepperModule,
    MatDialogModule,
    MatChipsModule,
    MatTableModule,
    MatIconModule,
    MatSnackBarModule,
    MatTabsModule,
    MatRadioModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
