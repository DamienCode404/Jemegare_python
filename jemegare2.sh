#!/usr/bin/env bash

if [ $# -ne 4 ]; then
		echo "$0 <adresse> <durée> <bmin> <nombre>" 1>&2
		echo "avec:     <adresse>  l'adresse de la position actuelle" 1>&2
		echo "          ""<durée>  la durée de stationnement prévue (en minutes)" 1>&2
    echo "          ""<bmin> le nombre minimum de places libres" 1>&2
		echo "et        <nombre> le nombre maximum de parkings à proposer" 1>&2
		exit 1
fi

chemin=~/jemegare
if [ ! -d $chemin ]; then
  mkdir $chemin | cd $chemin
fi

adresse=$chemin/adresses.json
dispo=$chemin/dispo.json
tarifications=$chemin/tarifications.json

if [ ! -f $adresse ]; then
  echo -n "Mise à jour de la base des adresses... "
  wget "https://data.nantesmetropole.fr/explore/dataset/244400404_adresses-postales-nantes-metropole/download/?format=json&timezone=Europe/Berlin&lang=fr" \
       -O $adresse 1>&2 2>/dev/null
fi
if [ ! -f $dispo ] || [ $(find $dispo -mmin +60) ]; then
  echo -n "Mise à jour de la base des disponibilités... "
  wget "https://data.nantesmetropole.fr/explore/dataset/244400404_parkings-publics-nantes-disponibilites/download/?format=json&timezone=Europe/Berlin&lang=fr" \
       -O $dispo 1>&2 2>/dev/null
fi
if [ ! -f $tarifications ] || [ $(find $tarifications -mtime +30) ]; then
  echo -n "Mise à jour de la base des tarifs... "
  wget "https://data.nantesmetropole.fr/explore/dataset/244400404_parkings-publics-nantes-tarification-horaire/download/?format=json&timezone=Europe/Berlin&lang=fr" \
       -O $tarifications 1>&2 2>/dev/null
fi

lattitude=$(./address2coords.py "adresses.json" "$1" | sed 's/^.//;s/.$//;s/,//' | cut -d " " -f 1)
longitude=$(./address2coords.py "adresses.json" "$1" | sed 's/^.//;s/.$//;s/,//' | cut -d " " -f 2)
if [ $? -ne 0 ]; then
		echo "l'adresse "$1" n'a pas été trouvée." 1>&2
		exit 6
fi
parking=$(./availabilities.py "dispo.json" "$3" | ./jemegare.py "tarifications.json" "$lattitude" "$longitude" "$2" | head -n $4)

echo "$parking\n"

