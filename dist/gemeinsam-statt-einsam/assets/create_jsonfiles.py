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
event["when"] = 1584898200
event["link"] = "https://www.twitch.tv/directory/game/Unreal%20Tournament"
event["video"] = "Twitch"
event["phone"] = "+49 69 18880"
event["phonepin"] = "18880"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Anderes"
event["name"] = "Skat mit Ulli"
event["description"] = "Skatabend mit Ulli"
event["when"] = 1584903600
event["link"] = "https://www.skat-spielen.de/"
event["video"] = "Skype"
event["phone"] = "+49 40 1234340"
event["phonepin"] = "1234340"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Anderes"
event["name"] = "Doppelkopf mit Bertram"
event["description"] = "Gefelgte Runde Doppelkopf mit gleichgesinnten."
event["when"] = 1584867600
event["link"] = "https://www.doppelkopf-palast.de/"
event["video"] = "Skype"
event["phone"] = "+49 30 1563462"
event["phonepin"] = "1563462"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Achtsamkeit"
event["name"] = "Meditation mit Geraldine"
event["description"] = "Zusammen meditieren um Gemeinsam zu sein"
event["when"] = 1584871200
event["link"] = "https://vedanta-yoga.de/online-meditations-kurs/"
event["video"] = "Discord"
event["phone"] = "+49 69 23232452"
event["phonepin"] = "23232452"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    

event["category"] = "Achtsamkeit"
event["name"] = "Qui Gong mit Albert"
event["description"] = "Qui Gong mit Albert. Auch für Einsteiger"
event["when"] = 1584900000
event["link"] = "https://qigongonline.de/"
event["video"] = "Zoom"
event["phone"] = "+49 30 248453452"
event["phonepin"] = "248453452"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Achtsamkeit"
event["name"] = "Progressive Muskelrelaxanz mit Maria"
event["description"] = "Gemeinsam daheim entspannen mit Maria"
event["when"] = 1584898200
event["link"] = "https://www.tk.de/techniker/magazin/life-balance/aktiv-entspannen/progressive-muskelentspannung-zum-download-2021142"
event["video"] = "Zoom"
event["phone"] = "+49 30 248453452"
event["phonepin"] = "248453452"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Unterhaltung"
event["name"] = "Heintje und Peter schauen"
event["description"] = "Gemeinsam den Film 'Heintje und Peter' schauen"
event["when"] = 1584889200
event["link"] = "https://www.zdf.de/kinder/heidi"
event["video"] = "ZDF Mediathek"
event["phone"] = "+49 30 7454523"
event["phonepin"] = "7454523"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Unterhaltung"
event["name"] = "Kevin allein Zuhaus schauen"
event["description"] = "Gemeinsam den Film 'Kevin allein Zuhaus' schauen"
event["when"] = 1584901800
event["link"] = "https://www.netflix.com/de/title/596983"
event["video"] = "Netflix"
event["phone"] = "+49 30 7454523"
event["phonepin"] = "7454523"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Unterhaltung"
event["name"] = "ACDC Live Konzert aus der Royal Albert Hall hören mit Elise "
event["description"] = "Endlich mal wieder abrocken mit ACDC"
event["when"] = 1584904500
event["link"] = "https://www.facebook.com/events/1292688854258527/"
event["video"] = "Facebook"
event["phone"] = "+49 30 711233"
event["phonepin"] = "711233"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Sport"
event["name"] = "Pilates mit Annika"
event["description"] = "Gemeinsam den Körper durch Pilates stärken"
event["when"] = 1584860400
event["link"] = "https://www.pilatesclub.de/"
event["video"] = "Zoom"
event["phone"] = "+49 30 711233"
event["phonepin"] = "711233"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    
event["category"] = "Sport"
event["name"] = "Tai Chi mit Herbert"
event["description"] = "Zur inneren Ruhe finden mit Tai Chi"
event["when"] = 1584862200
event["link"] = "http://www.tai-chi-zentrum.de/e-clips-tai-chi.htm"
event["video"] = "Skype"
event["phone"] = "+49 69 456233"
event["phonepin"] = "456233"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Sport"
event["name"] = "Yoga mit Hannah"
event["description"] = "Gemeinsames Yoga mit Hannah aus Mainz"
event["when"] = 1584856800
event["link"] = "https://www.lu-yoga.de/stundenplan/"
event["video"] = "Skype"
event["phone"] = "+49 6131 734343"
event["phonepin"] = "734343"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Treffen"
event["name"] = "Kuchen mit Bertram"
event["description"] = "Lust auf ein Stück Kuchen? Gemeinsam mit Bertram treffen und sich über dies und das Unterhalten bei einem leckeren Stück Kuchen."
event["when"] = 1584882000
event["link"] = "https://www.deinetorte.de/"
event["video"] = "Skype"
event["phone"] = "+49 761 73434"
event["phonepin"] = "73434"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)

event["category"] = "Treffen"
event["name"] = "Pizza mit Gundula "
event["description"] = "Pizzaabend mit Gundula."
event["when"] = 1584896400
event["link"] = "https://www.lieferando.de/"
event["video"] = "Telegram"
event["phone"] = "+49 30 874523"
event["phonepin"] = "874523"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    
event["category"] = "Treffen"
event["name"] = "Kaffee und Kuchen mit Gert"
event["description"] = "lust auf ein nettes Gespräch bei Kaffe und Kuchen?"
event["when"] = 1584896400
event["link"] = "https://www.ditsch.de/de/"
event["video"] = "Discord"
event["phone"] = "+49 30 874523"
event["phonepin"] = "874523"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    
event["category"] = "Treffen"
event["name"] = "Weinabend mit Thees"
event["description"] = "'Du bringst die Story - ich bring den Wein'"
event["when"] = 1584905400
event["link"] = "https://www.keinweindenfaschisten.de/#Home"
event["video"] = "Zoom"
event["phone"] = "+49 40 874523"
event["phonepin"] = "874523"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    
event["category"] = "Unterhaltung"
event["name"] = "Kneipenabend mit Yassin"
event["description"] = "Feierabendbier mit Yassin aus Berlin."
event["when"] = 1584909000
event["link"] = "http://www.kessel-darmstadt.de/"
event["video"] = "Zoom"
event["phone"] = "+49 6150 31235"
event["phonepin"] = "31235"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    
event["category"] = "Treffen"
event["name"] = "Tatort mit Jochen"
event["description"] = "Niemals ohne mich \n Eine Mitarbeiterin des Jugendamtes wird erschlagen aufgefunden, nicht weit entfernt von ihrer Wohnung. Bei ihren Ermittlungen stoßen die Hauptkommissare Ballauf und Schenk auf getrennte Elternpaare, die gegeneinander kämpfen."
event["when"] = 1584905400
event["link"] = "https://www.ardmediathek.de/ard/shows/Y3JpZDovL2Rhc2Vyc3RlLmRlL3RhdG9ydA/tatort"
event["video"] = "Discord"
event["phone"] = "+49 6150 31235"
event["phonepin"] = "31235"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)
    
event["category"] = "Unterhaltung"
event["name"] = "ESL ProLeague Season 11"
event["description"] = "Astralis vs Team Spirit - kann Astralis nochmal zurückschlagen? "
event["when"] = 1584896400
event["link"] = "https://www.twitch.tv/esl_csgo"
event["video"] = "Twitch"
event["phone"] = "+49 89 5712335"
event["phonepin"] = "5712335"

with open(event["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(event, outfile)