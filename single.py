
## Import libraries

import requests
import time

##We will use as URL a simple request / response webserivce

start = time.time()
URL = 'https://httpbin.org/uuid'

def capture(session, url):
    with session.get(url) as r:
        print(r.json()['uuid'])


def main():
    with requests.Session() as s:
        for _ in range(100):
            capture(s,URL)

main()

# python 3
print('It took', time.time()-start, 'seconds.')

### It took 19.225637197494507 seconds.