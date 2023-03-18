#!/usr/bin/env python3
import sys
import json
parking_available = []
if len(sys.argv) < 3:
    print(f"Appel: {sys.argv[0]} <fichier de disponibilités> <bornemin>", file=sys.stderr)
    exit(1)
try :
    bornemin = int(sys.argv[2])
except ValueError:
    print(f"L'argument {sys.argv[2]} doit être numérique!",file=sys.stderr)
    exit(1)
with open(sys.argv[1]) as content:
    data = json.load(content)
    for rec in data:
        numero = rec['fields']['idobj']
        if bornemin < rec['fields']['disponibilite'] :
            parking_available.append(numero)
if len(parking_available)==0:
	print("Pas de parking disponible avec ces conditions")
else:
    for i in parking_available:
        print(i)

"""print(parking_available)"""

