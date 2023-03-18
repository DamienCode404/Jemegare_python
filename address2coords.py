#!/usr/bin/env python3
import sys
import json
if len(sys.argv) < 3:
    print(f"Appel: {sys.argv[0]} <fichier adresse JSON> <adresse>", file=sys.stderr)
    exit(1)
adresse = sys.argv[2].encode('latin-1').lower()
with open(sys.argv[1]) as content:
    data = json.load(content)
    for rec in data:
        fields = rec['fields']
        coordonnee = fields['geo_shape']['coordinates']
        if fields['adresse'].encode('latin-1').lower() == adresse:
            print(coordonnee)
            exit(0)
print(f"Impossible de trouver l'adresse demandée {sys.argv[2]}.",file=sys.stderr)
exit(2)