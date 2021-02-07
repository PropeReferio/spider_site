import requests
import time

start = time.time()
with open('./wordlists/namelist.txt', 'r') as wordlist:
    for line in wordlist:
        cur_url = f"https://facialabused.wordpress.com/{line}"
        r = requests.get(cur_url)
        if r.status_code not in [400, 404]:
            print(f"Page found: {cur_url}\nStatus Code: {r.status_code}")

print(f"Total time: {time.time() - start}")
#Took 4 minutes