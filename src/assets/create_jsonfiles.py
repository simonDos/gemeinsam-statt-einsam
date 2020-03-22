# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import json
import datetime,time

import glob
 # inital event
result={}
event={}


#event["category"] = "Anderes"
ut={}
ut["name"] = "Unreal Tournament mit Johanns"
ut["description"] = "FPS max und los geht's"
ut["when"] = 1584898200
ut["link"] = "https://www.twitch.tv/directory/game/Unreal%20Tournament"
ut["video"] = "Twitch"
ut["phone"] = "+49 69 18880"
ut["phonepin"] = "18880"
result["Anderes"] = ut
with open(ut["name"].replace(" ","")+'.json', 'w') as outfile:
     json.dump(result, outfile)
    
#outfile.close()
skat={}
#event["category"] = "Anderes"
skat["name"] = "Skat mit Ulli"
skat["description"] = "Skatabend mit Ulli"
skat["when"] = 1584903600
skat["link"] = "https://www.skat-spielen.de/"
skat["video"] = "Skype"
skat["phone"] = "+49 40 1234340"
skat["phonepin"] = "1234340"

result["Anderes"] = skat

with open(skat["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)

# outfile.close()



#event["category"] = "Anderes"
dk={}
dk["name"] = "Doppelkopf mit Bertram"
dk["description"] = "Gefelgte Runde Doppelkopf mit gleichgesinnten."
dk["when"] = 1584867600
dk["link"] = "https://www.doppelkopf-palast.de/"
dk["video"] = "Skype"
dk["phone"] = "+49 30 1563462"
dk["phonepin"] = "1563462"
result["Anderes"] = dk

with open(dk["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
 

#event["category"] = "Achtsamkeit"
medi={}
medi["name"] = "Meditation mit Geraldine"
medi["description"] = "Zusammen meditieren um Gemeinsam zu sein"
medi["when"] = 1584871200
medi["link"] = "https://vedanta-yoga.de/online-meditations-kurs/"
medi["video"] = "Discord"
medi["phone"] = "+49 69 23232452"
medi["phonepin"] = "23232452"

result["Achtsamkeit"] = medi
with open(medi["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)


    
#event["category"] = "Achtsamkeit"
quigong={}
quigong["name"] = "Qui Gong mit Albert"
quigong["description"] = "Qui Gong mit Albert. Auch für Einsteiger"
quigong["when"] = 1584900000
quigong["link"] = "https://qigongonline.de/"
quigong["video"] = "Zoom"
quigong["phone"] = "+49 30 248453452"
quigong["phonepin"] = "248453452"

result["Achtsamkeit"] = quigong
with open(quigong["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    
#event["category"] = "Achtsamkeit"
promusk={}
promusk["name"] = "Progressive Muskelrelaxanz mit Maria"
promusk["description"] = "Gemeinsam daheim entspannen mit Maria"
promusk["when"] = 1584898200
promusk["link"] = "https://www.tk.de/techniker/magazin/life-balance/aktiv-entspannen/progressive-muskelentspannung-zum-download-2021142"
promusk["video"] = "Zoom"
promusk["phone"] = "+49 30 248453452"
promusk["phonepin"] = "248453452"
result["Achtsamkeit"] = promusk
with open(promusk["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    
#event["category"] = "Unterhaltung"
film1={}
film1["name"] = "Heintje und Peter schauen"
film1["description"] = "Gemeinsam den Film 'Heintje und Peter' schauen"
film1["when"] = 1584889200
film1["link"] = "https://www.zdf.de/kinder/heidi"
film1["video"] = "ZDF Mediathek"
film1["phone"] = "+49 30 7454523"
film1["phonepin"] = "7454523"

result["Unterhaltung"] = film1
with open(film1["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    
#event["category"] = "Unterhaltung"
film2={}
film2["name"] = "Kevin allein Zuhaus schauen"
film2["description"] = "Gemeinsam den Film 'Kevin allein Zuhaus' schauen"
film2["when"] = 1584901800
film2["link"] = "https://www.netflix.com/de/title/596983"
film2["video"] = "Netflix"
film2["phone"] = "+49 30 7454523"
film2["phonepin"] = "7454523"

result["Unterhaltung"] = film2
with open(film2["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
    
# outfile.close()
     
#event["category"] = "Unterhaltung"
acdc={}
acdc["name"] = "ACDC Live Konzert aus der Royal Albert Hall hören mit Elise "
acdc["description"] = "Endlich mal wieder abrocken mit ACDC"
acdc["when"] = 1584904500
acdc["link"] = "https://www.facebook.com/events/1292688854258527/"
acdc["video"] = "Facebook"
acdc["phone"] = "+49 30 711233"
acdc["phonepin"] = "711233"
result["Unterhaltung"] = acdc
with open(acdc["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
#outfile.close()
    
#event["category"] = "Sport"
pilates={}
pilates["name"] = "Pilates mit Annika"
pilates["description"] = "Gemeinsam den Körper durch Pilates stärken"
pilates["when"] = 1584860400
pilates["link"] = "https://www.pilatesclub.de/"
pilates["video"] = "Zoom"
pilates["phone"] = "+49 30 711233"
pilates["phonepin"] = "711233"

result["Sport"] = pilates
with open(pilates["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    
    
#event["category"] = "Sport"
taichi={}
taichi["name"] = "Tai Chi mit Herbert"
taichi["description"] = "Zur inneren Ruhe finden mit Tai Chi"
taichi["when"] = 1584862200
taichi["link"] = "http://www.tai-chi-zentrum.de/e-clips-tai-chi.htm"
taichi["video"] = "Skype"
taichi["phone"] = "+49 69 456233"
taichi["phonepin"] = "456233"

result["Sport"] = taichi
with open(taichi["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    

#event["category"] = "Sport"
yoga={}
yoga["name"] = "Yoga mit Hannah"
yoga["description"] = "Gemeinsames Yoga mit Hannah aus Mainz"
yoga["when"] = 1584856800
yoga["link"] = "https://www.lu-yoga.de/stundenplan/"
yoga["video"] = "Skype"
yoga["phone"] = "+49 6131 734343"
yoga["phonepin"] = "734343"

result["Sport"] = yoga
with open(yoga["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    

#event["category"] = "Treffen"
kuchen={}
kuchen["name"] = "Kuchen mit Bertram"
kuchen["description"] = "Lust auf ein Stück Kuchen? Gemeinsam mit Bertram treffen und sich über dies und das Unterhalten bei einem leckeren Stück Kuchen."
kuchen["when"] = 1584882000
kuchen["link"] = "https://www.deinetorte.de/"
kuchen["video"] = "Skype"
kuchen["phone"] = "+49 761 73434"
kuchen["phonepin"] = "73434"

result["Treffen"] = kuchen
with open(kuchen["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    
#event["category"] = "Treffen"
pizza={}
pizza["name"] = "Pizza mit Gundula "
pizza["description"] = "Pizzaabend mit Gundula."
pizza["when"] = 1584896400
pizza["link"] = "https://www.lieferando.de/"
pizza["video"] = "Telegram"
pizza["phone"] = "+49 30 874523"
pizza["phonepin"] = "874523"

result["Treffen"] = pizza
with open(pizza["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    
#event["category"] = "Treffen"
kaffe={}
kaffe["name"] = "Kaffee und Kuchen mit Gert"
kaffe["description"] = "lust auf ein nettes Gespräch bei Kaffe und Kuchen?"
kaffe["when"] = 1584896400
kaffe["link"] = "https://www.ditsch.de/de/"
kaffe["video"] = "Discord"
kaffe["phone"] = "+49 30 874523"
kaffe["phonepin"] = "874523"

result["Treffen"] = kaffe
with open(kaffe["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
       
#event["category"] = "Treffen"
wein={}
wein["name"] = "Weinabend mit Thees"
wein["description"] = "'Du bringst die Story - ich bring den Wein'"
wein["when"] = 1584905400
wein["link"] = "https://www.keinweindenfaschisten.de/#Home"
wein["video"] = "Zoom"
wein["phone"] = "+49 40 874523"
wein["phonepin"] = "874523"
result["Treffen"] = wein
with open(wein["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
        
#event["category"] = "Unterhaltung"
kneipe={}
kneipe["name"] = "Kneipenabend mit Yassin"
kneipe["description"] = "Feierabendbier mit Yassin aus Berlin."
kneipe["when"] = 1584909000
kneipe["link"] = "http://www.kessel-darmstadt.de/"
kneipe["video"] = "Zoom"
kneipe["phone"] = "+49 6150 31235"
kneipe["phonepin"] = "31235"

result["Unterhaltung"] = kneipe
with open(kneipe["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
      
#event["category"] = "Treffen"
tatort={}
tatort["name"] = "Tatort mit Jochen"
tatort["description"] = "Niemals ohne mich \n Eine Mitarbeiterin des Jugendamtes wird erschlagen aufgefunden, nicht weit entfernt von ihrer Wohnung. Bei ihren Ermittlungen stoßen die Hauptkommissare Ballauf und Schenk auf getrennte Elternpaare, die gegeneinander kämpfen."
tatort["when"] = 1584905400
tatort["link"] = "https://www.ardmediathek.de/ard/shows/Y3JpZDovL2Rhc2Vyc3RlLmRlL3RhdG9ydA/tatort"
tatort["video"] = "Discord"
tatort["phone"] = "+49 6150 31235"
tatort["phonepin"] = "31235"

result["Treffen"] = tatort
with open(tatort["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# outfile.close()
    
#category={}
#category["category"] = "Unterhaltung"
esl={}
esl["name"] = "ESL ProLeague Season 11"
esl["description"] = "Astralis vs Team Spirit - kann Astralis nochmal zurückschlagen? "
esl["when"] = 1584896400
esl["link"] = "https://www.twitch.tv/esl_csgo"
esl["video"] = "Twitch"
esl["phone"] = "+49 89 5712335"
esl["phonepin"] = "5712335"
result["Unterhaltung"] = esl

with open(esl["name"].replace(" ","")+'.json', 'w') as outfile:
    json.dump(result, outfile)
# #outfile.close()
    
      
events = []
events.append(film1)
events.append(kaffe)
events.append(esl)
events.append(kuchen)
events.append(medi)
events.append(film2)
events.append(dk)
events.append(acdc)
events.append(kneipe)
events.append(wein)
events.append(kuchen)
events.append(pilates)
events.append(pizza)
events.append(promusk)
events.append(quigong)
events.append(skat)
events.append(taichi)
events.append(tatort)
events.append(ut)
events.append(yoga)


with open("merged_file.json", "w", encoding="utf8") as outfile:
     json.dump(events, outfile)