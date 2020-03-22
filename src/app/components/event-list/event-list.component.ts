import { Component, OnInit, Input } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table'
import {EventsEntry} from '../../classes/EventsEntry'



@Component({
  selector: 'app-event-list',
  templateUrl: './event-list.component.html',
  styleUrls: ['./event-list.component.scss']
})
export class EventListComponent implements OnInit {

  @Input() events: EventsEntry[]

  _events: any

  displayedColumns: string[] = ['event', 'when', 'how']

  constructor() { 
    this._events = new MatTableDataSource(this.events)
  }

  ngOnInit(): void {
  }

}
