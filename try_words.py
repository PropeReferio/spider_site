import requests
import time
import random

start = time.time()

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]


with open('./wordlists/real_paths.txt', 'r') as wordlist:
    for line in wordlist:
        cur_url = f"https://coder.today/{line}"
        headers = {'user-agent': random.choice(user_agent_list)}
        r = requests.get(cur_url, headers=headers)
        if r.status_code not in [400, 404]:
            print(f"Page found: {cur_url}\nStatus Code: {r.status_code}")

print(f"Total time: {time.time() - start}")
#Took 4 minutes