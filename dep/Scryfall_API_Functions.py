# -*coding: utf-8 -*-
"""
Created on Sat Jun 28 11:29:42 2025

@author: Arees
"""
import requests

def call_standard_cards():
    import time
    base_url = "https://api.scryfall.com/cards/search"
    all_cards = []
    page = 1
    has_more = True
    headers = {'User-Agent': 'Standard_Playable', 'Accept': '*/*'}
    while has_more:
        params = {
            "q": "legal:standard",
            "page": page
        }
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()   
        data = response.json()
        all_cards.extend(data["data"])
        print('Cards from page %i saved' % (page,))
        time.sleep(.2)
        has_more = data["has_more"]
        page += 1
    return all_cards

def standard_cards_check(x):
    from pathlib import Path
    import json
    with open('most_recent_standard_dataset.txt', 'r') as txt_file:
        standard_file_name = txt_file.read().rstrip()
    current_dir = Path(__file__).parent
    most_recent_loc = (current_dir / '..' / 'Data/Standard-Cards' / standard_file_name).resolve()
    with open(most_recent_loc, 'r') as file:
        most_recent_standard_cards = json.load(file)
    new_cards = False
    if len(x) == len(most_recent_standard_cards):
        print('Their are not any new cards to be updated')
    else:
        new_cards = True
    return new_cards

def json_save(x):
    import json
    from datetime import date
    date = str(date.today())
    file_name = 'standard-cards-' + date + '.json'
    file_location = '../Data/Standard-Cards/' + file_name
    with open(file_location, 'w') as output_file:
        json.dump(x, output_file, indent=2)
    print('Standard card data saved at', file_location)
    text_file_name = 'most_recent_standard_dataset.txt'
    with open(text_file_name, 'w', encoding='utf-8') as file:
        file.write(file_name)
    print('Text file overwritten with', file_name)
    return (file_name)



