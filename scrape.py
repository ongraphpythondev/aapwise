import json
from scrape_play_store_app_data.main import scrap_using_url

def process_data(data):
    print(data["name"])
    print(type(data["name"]))
    message=scrap_using_url(data["name"])
    return { "message": message }

