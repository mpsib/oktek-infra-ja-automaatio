# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.
# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500
import json
import urllib.request

def haeAineisto():
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        file = response.read()
    return json.loads(file)

def haePostinumerot(postitoimipaikka, aineisto):
    tulokset = []

    for postinumero, toimipaikka in aineisto.items():
        if toimipaikka.replace(' ', '') == postitoimipaikka.upper().replace(' ', ''):
            tulokset.append(postinumero)

    tulokset.sort()
    return tulokset

def tulostaTulokset(tulokset):
    if len(tulokset) > 0:
        response = 'Postinumerot: '
        for postinumero in tulokset:
            response = response + postinumero + ', '
        return response[:-2]
    else:
        return 'Tuntematon postitoimipaikka'

if __name__ == '__main__':
    postitoimipaikka = input('Kirjoita postitoimipaikka: ')
    print(tulostaTulokset(haePostinumerot(postitoimipaikka, haeAineisto())))