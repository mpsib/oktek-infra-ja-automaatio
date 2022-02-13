# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.
# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500
import json
import urllib.request

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
   file = response.read()

aineisto = json.loads(file)

tulokset = []
postitoimipaikka = input('Kirjoita postitoimipaikka: ').upper()

for postinumero, toimipaikka in aineisto.items():
    if toimipaikka == postitoimipaikka:
        tulokset.append(postinumero)


if len(tulokset) > 0:
    tulokset.sort()
    response = 'Postinumerot: '
    for postinumero in tulokset:
        response = response + postinumero + ', '
    print(response[:-2])
else:
    print('Tuntematon postitoimipaikka')