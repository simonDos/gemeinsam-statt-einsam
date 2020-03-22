import { Component, OnInit } from "@angular/core";
import { EventsEntry } from "src/app/classes/EventsEntry";

@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.scss"]
})
export class DashboardComponent implements OnInit {
  essen_events: EventsEntry[] = []

  my_events: EventsEntry[] = []

  constructor() {

    this.essen_events.push(
      new EventsEntry(
        "Frühstück",
        "Wir frühstücken zusammen! :)",
        1584871200,
        "chefkoch.de",
        "jitsi.org",
        "+49 1234567890",
        "789 345"
      )
    );

    this.essen_events.push(
      new EventsEntry(
        "Frühstück",
        "Wir frühstücken zusammen! :)",
        1584871200,
        "chefkoch.de",
        "jitsi.org",
        "+49 1234567890",
        "789 345"
      )
    );

  

    

    this.my_events.push(
      new EventsEntry(
        "Frühstück",
        "Wir frühstücken zusammen! :)",
        1584871200,
        "chefkoch.de",
        "jitsi.org",
        "+49 1234567890",
        "789 345"
      )
    );

    this.my_events.push(
      new EventsEntry(
        "Frühstück",
        "Wir frühstücken zusammen! :)",
        1584871200,
        "chefkoch.de",
        "jitsi.org",
        "+49 1234567890",
        "789 345"
      )
    );

    this.my_events.push(
      new EventsEntry(
        "Frühstück",
        "Wir frühstücken zusammen! :)",
        1584871200,
        "chefkoch.de",
        "jitsi.org",
        "+49 1234567890",
        "789 345"
      )
    );
  }

  ngOnInit(): void {}
}
