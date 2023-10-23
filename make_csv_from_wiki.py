import csv
import re
from typing import Any

import requests
from bs4 import BeautifulSoup


def find_prefecture(td_list: list) -> str:
    pref_value = td_list[1].find('a')
    if pref_value is not None:
        is_prefecture = True if re.match('^/wiki/*', pref_value.get('href')) else False
        if is_prefecture:
            return pref_value.get_text()
        else:
            return prefecture
    else:
        return prefecture


def find_plate_name(td_list: list) -> Any | None:
    for td in td_list:
        if td.find('b') is not None:
            return td.find('b').get_text()
        else:
            continue
    else:
        return None


prefecture = ''
plate_name = ''
csv_col1 = 'prefecture'
csv_col2 = 'plate_name'

URL = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%8A%E3%83%B3%E3%83%90%E3%83%BC%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E4%B8%80%E8%A6%A7'
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

with open('number_plate.csv', 'w') as csv_f:
    fieldnames = [csv_col1, csv_col2]
    writer = csv.DictWriter(csv_f, fieldnames)
    writer.writeheader()
    for row in soup.find('table', class_='wikitable').find('tbody').find_all('tr')[1:]:
        prefecture = find_prefecture(row.find_all('td'))
        plate_name = find_plate_name(row.find_all('td'))
        if plate_name is not None:
            writer.writerow({csv_col1: prefecture, csv_col2: plate_name})
