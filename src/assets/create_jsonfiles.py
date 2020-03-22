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
event_category=["Treffen","Sport","Unterhaltung","Achtsamkeit","Anderes"]
event_name=["Yoga","Meditieren","Frühstück","30-Min Trimm dich"]

event_video=["skype","zoom","whatspp","n/a","discord","telegram"]

event["category"] = event_category[0]
event["name"] = "test"
event["description"] = "hier ist beschreibung"
event["when"] = timestamp
event["link"] = "www.chefkoch.de"
event["video"] = event_video[0]
event["phone"] = "+49 49 18880"
event["phonepin"] = "18880"


with open('data_example.json', 'w') as outfile:
    json.dump(event, outfile)
