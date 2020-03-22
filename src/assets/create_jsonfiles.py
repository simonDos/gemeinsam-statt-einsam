# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import json
import datetime,time
import random

event={} # inital event

today = datetime.date.today()
first = today.replace(day=6)
lastMonth = first - datetime.timedelta(days=6) 
timestamp = time.mktime(lastMonth.timetuple())


event["category"] = "Anderes"
event["name"] = "Unreal Tournament mit Johanns"
event["description"] = "FPS max und los geht's"
event["when"] = timestamp
event["link"] = "localhost:7777"
event["video"] = "Twitch"
event["phone"] = "+49 69 18880"
event["phonepin"] = "18880"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Anderes"
event["name"] = "Skat mit Ulli"
event["description"] = "Skatabend mit Ulli"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Skype"
event["phone"] = "+49 40 1234340"
event["phonepin"] = "1234340"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Anderes"
event["name"] = "Doppelkopf mit Bertram"
event["description"] = "Gefelgte Runde Doppelkopf mit gleichgesinnten."
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Skype"
event["phone"] = "+49 30 1563462"
event["phonepin"] = "1563462"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Achtsamkeit"
event["name"] = "Meditation mit Geraldine"
event["description"] = "Zusammen meditieren um Gemeinsam zu sein"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Discord"
event["phone"] = "+49 69 23232452"
event["phonepin"] = "23232452"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    

event["category"] = "Achtsamkeit"
event["name"] = "Qui Gong mit Albert"
event["description"] = "Qui Gong mit Albert. Auch für Einsteiger"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Zoom"
event["phone"] = "+49 30 248453452"
event["phonepin"] = "248453452"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Achtsamkeit"
event["name"] = "Progressive Muskelrelaxanz mit Maria"
event["description"] = "Gemeinsam daheim entspannen mit Maria"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Zoom"
event["phone"] = "+49 30 248453452"
event["phonepin"] = "248453452"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Unterhaltung"
event["name"] = " 'Heintje und Peter' schauen"
event["description"] = "Gemeinsam den Film 'Heintje und Peter' schauen"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Netflix"
event["phone"] = "+49 30 7454523"
event["phonepin"] = "7454523"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Unterhaltung"
event["name"] = " 'Kevin allein Zuhaus' schauen"
event["description"] = "Gemeinsam den Film 'Kevin allein Zuhaus' schauen"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Netflix"
event["phone"] = "+49 30 7454523"
event["phonepin"] = "7454523"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Unterhaltung"
event["name"] = " ACDC Live Konzert aus der Royal Albert Hall hören mit Elise "
event["description"] = "Endlich mal wieder abrocken mit ACDC"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Facebook"
event["phone"] = "+49 30 711233"
event["phonepin"] = "711233"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Sport"
event["name"] = "Pilates mit Annika"
event["description"] = "Gemeinsam den Körper durch Pilates stärken"
event["when"] = timestamp
event["link"] = "-"
event["video"] = "Facebook"
event["phone"] = "+49 30 711233"
event["phonepin"] = "711233"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    
    

