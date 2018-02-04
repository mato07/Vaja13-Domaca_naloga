from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import random

MAIN_URL = "http://quotes.yourdictionary.com/theme/marriage/"

webpage = urlopen(MAIN_URL).read()
nice_webpage = BeautifulSoup(webpage)

misli = nice_webpage.findAll("p", {"class": "quoteContent"})

pos_misli = []

for i, misel in enumerate(misli):
    pos_misli.append(misel.text)

izbira = []
for i in range(5):
    while True:
        nakljucno_stevilo = random.randint(1, len(pos_misli))
        if nakljucno_stevilo not in izbira:
            break
    izbira.append(nakljucno_stevilo)


for i, izbrano_stevilo in enumerate(izbira):
    print str(i+1) + ") " + pos_misli[izbrano_stevilo]


