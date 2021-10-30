import requests
import json
from datetime import datetime


def get_matches():
    date = datetime.today().strftime('%Y-%m-%d')

    url = "https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=" + '2021-10-20' + "&endDate=" + date
    page = requests.get(url)
    if page.status_code == 403:
        return None
    elif page.status_code == 404:
        return None
    else:
        pass
    apidata = page.json()
    apidata['dates']
    game_list= []
    for index in apidata['dates']:
        tuple = (index['games'][0]['teams']['away']['team']['name'],index['games'][0]['teams']['home']['team']['name'])
        game_list.append(tuple)
    return game_list