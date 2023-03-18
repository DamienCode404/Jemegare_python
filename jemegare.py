#!/usr/bin/env python3
import sys
import json
import distance
import time
from operator import itemgetter

duree = int(sys.argv[4])
liste_parking = []
classement = {}
t = time.localtime()
heure_actuelle = int(time.strftime("%H",t))
if 8 <= heure_actuelle <= 19:
    tarif = "normal"
else:
    tarif = "nuit"

if len(sys.argv) != 5:
    print(f"Appel: {sys.argv[0]} <fichier des tarifs> <latitude> <longitude> <durée stationnement en minutes>", file=sys.stderr)
    exit(1)
try :
    latitude1 = float(sys.argv[2])
    longitude1 = float(sys.argv[3])
except ValueError:
    print(f"Les arguments {sys.argv[2]} et {sys.argv[3]} doivent être numérique!",file=sys.stderr)
    exit(1)

for number in sys.stdin :
    dispo = int(number)
    with open(sys.argv[1]) as content:
        data = json.load(content)
        for rec in data:
            value = int(rec['fields']['idobj'])
            if dispo == value:
                nom = rec['fields']['nom_du_parking']
                latitude2 = rec['fields']['location'][1]
                longitude2 = rec['fields']['location'][0]
                if tarif == "normal":
                    if 0 <= duree < 10:
                        prix = rec['fields']['10min']
                    if 10 <= duree < 20:
                        prix = rec['fields']['20min']
                    elif 20 <= duree < 30:
                        prix = rec['fields']['30min']
                    elif 30 <= duree < 40:
                        prix = rec['fields']['40min']
                    elif 40 <= duree < 50:
                        prix = rec['fields']['50min']
                    elif 50 <= duree < 60:
                        prix = rec['fields']['1h']
                    elif 60 <= duree < 90:
                        prix = rec['fields']['1h30']
                    elif 90 <= duree < 120:
                        prix = rec['fields']['2h']
                    elif 120 <= duree < 150:
                        prix = rec['fields']['2h30']
                    elif 150 <= duree < 180:
                        prix = rec['fields']['3h']
                    elif 660 >= duree :
                        prix = rec['fields']['11h']
                else:
                    try :
                        if 0 <= duree < 10:
                            prix = rec['fields']['nuit_10min']
                        if 10 <= duree < 20:
                            prix = rec['fields']['nuit_20min']
                        elif 20 <= duree < 30:
                            prix = rec['fields']['nuit_30min']
                        elif 30 <= duree < 40:
                            prix = rec['fields']['nuit_40min']
                        elif 40 <= duree < 50:
                            prix = rec['fields']['nuit_50min']
                        elif 50 <= duree < 60:
                            prix = rec['fields']['nuit_1h']
                        elif 60 <= duree < 90:
                            prix = rec['fields']['nuit_1h30']
                        elif 90 <= duree < 120 :
                            prix = rec['fields']['nuit_2h']
                        elif 120 <= duree < 150:
                            prix = rec['fields']['nuit_2h30']
                        elif 150 <= duree < 180:
                            prix = rec['fields']['nuit_3h']
                        elif duree >= 660:
                            prix = rec['fields']['11h']
                    except KeyError:
                        print("il n'y a pas de tarif de nuit pour ce parking")

                trajet = distance.distance(latitude1, longitude1, latitude2, longitude2)
                classement[trajet] = (nom,prix)
liste_parking = sorted(classement.items(), key=lambda item:item[0])
for i in range(len(liste_parking)):
    print(liste_parking[i][1][0],':',liste_parking[i][1][1], "euros")






        
        
