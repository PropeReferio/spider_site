import requests
import time

start = time.time()

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0'}
with open('./wordlists/real_paths.txt', 'r') as wordlist:
    for line in wordlist:
        cur_url = f"https://w3schools.com/{line}"
        r = requests.get(cur_url, headers=headers)
        if r.status_code not in [400, 404]:
            print(f"Page found: {cur_url}\nStatus Code: {r.status_code}")

print(f"Total time: {time.time() - start}")
#Took 4 minutes