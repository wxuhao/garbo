# https://www.epochconverter.com/webkit
import time
import os
import json
from bs4 import BeautifulSoup as bs


# Get current webkit time (microseconds)
def webkit_time_now():
    # epoch time + EPOCH_CONSTANT_SEC = webkit time in sec
    EPOCH_CONSTANT_SEC = 11_643_609_600
    return (time.time() + EPOCH_CONSTANT_SEC) * 1_000_000

def recursive_add_to_dict(struct, add_to_set):
    if isinstance(struct, dict):
        if 'url' in struct:
            added_urls.add(struct['url'])
            return
        for item in struct:
            recursive_add_to_dict(struct[item], add_to_set)
    elif isinstance(struct, list):
        for item in struct:
            recursive_add_to_dict(item, add_to_set)

os.chdir(r"C:\Users\xuhao's PC\AppData\Local\Google\Chrome\User Data\Default")
with open('Bookmarks', encoding="utf-8") as bm_json:
    bookmarks = json.loads(bm_json.read())
    
    # Keep track of links that have already been added to bookmarks
    added_urls = set()
    recursive_add_to_dict(bookmarks, added_urls)
    
