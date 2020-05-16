import re

from unidecode import unidecode


def split(chain, sep, pos):
    chain = chain.split(sep)
    return sep.join(chain[:pos]), sep.join(chain[pos:])


def normalice_town_name(list_towns):
    towns_temp = []
    for item in list_towns:

        item = split(item, '-', 1)
        place_tmp = item[1].strip().split(',')
        place = (
            f'{place_tmp[1].strip()} {place_tmp[0].strip()}'
            if len(place_tmp) > 1
            else place_tmp[0]
        )
        towns_temp.append(f'{place}, Madrid')

    return towns_temp


def normalize_name(name):
    return re.sub(r'\W', '_', unidecode(name.strip().lower()))
