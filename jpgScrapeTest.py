import requests
url = 'https://pbs.twimg.com/media/Cjq2Fw2WEAAOozl.jpg'
r = requests.get(url)
open('../Desktop/test.jpg', 'wb').write(r.content)
#https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un
