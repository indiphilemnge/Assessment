import os

import requests

site = ["http://api.open-notify.org/astros.json"]
times = os.environ ['times']

TOTAL= 0
for i in range(len(site)):
    if TOTAL < times :
        s = requests.get(site[i])
        total = s.elapsed
        print ('site:' , site[i])
        print ("Time: ", s.elapsed)
        print ('Total of number of hits:', times)
