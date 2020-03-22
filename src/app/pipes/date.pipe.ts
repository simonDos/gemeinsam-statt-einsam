import {Pipe, PipeTransform} from '@angular/core'
import { DomSanitizer } from '@angular/platform-browser'

@Pipe({
  name: 'datepipe'
})

export class DatePipe implements PipeTransform {

  transform(timestamp: number, args?: any): any {

    if (!timestamp) {
      return null
    }

    console.log(timestamp)

    const date = new Date(timestamp * 1000)

    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };

    return date.toLocaleTimeString("de-DE", options)
  }
}
