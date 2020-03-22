import { Component, OnInit, Input } from "@angular/core";
import { EventsEntry } from "src/app/classes/EventsEntry";

@Component({
  selector: "app-plan",
  templateUrl: "./plan.component.html",
  styleUrls: ["./plan.component.scss"]
})
export class PlanComponent implements OnInit {
  @Input() events: EventsEntry[];

  constructor(

  ) {}

  ngOnInit(): void { }
  
  goTo = (link: string) => {
    window.open("https://" + link)
  }
}


