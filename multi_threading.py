
## Import libraries

from regex import R
import requests
import time
import threading

##We will use as URL a simple request / response webserivce

start = time.time()
URL = 'https://httpbin.org/uuid'

def capture():
    #for _ in range(100):
    r = requests.get(URL)
    print(r.json()['uuid'])
    
def main():
    threads = []
    
    for i in range(100):
        t = threading.Thread(target = capture)
        t.daemon = True
        threads.append(t)

    
    for i in range(100):
        threads[i].start()
    
    for i in range(100):
        threads[i].join()

    
        
            

main()

# python 3
print('It took', time.time()-start, 'seconds.')

### It took 3.10 seconds.