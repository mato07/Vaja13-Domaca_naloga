from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

MAIN_URL = "https://en.wikipedia.org/wiki/Game_of_Thrones"
SUBMAIN_URL = "https://en.wikipedia.org"

webpage = urlopen(MAIN_URL).read()
nice_webpage = BeautifulSoup(webpage)

st_sezon = 7
st_gledalcev = 0

for i in range(1,st_sezon+1):
    sezonska_stran = BeautifulSoup(urlopen(SUBMAIN_URL + "/wiki/Game_of_Thrones_(season_%s)" %i).read())
    tabele = sezonska_stran.find("table", {"class": "wikitable plainrowheaders wikiepisodetable"})
    if tabele:
        epizode = tabele.findAll('tr', attrs={'class': 'vevent'})

        if epizode:
            for epizoda in epizode:
                st_ogledov = str(epizoda.findAll('td')[-1])
                stevilo = float(st_ogledov[st_ogledov.find(">")+1:st_ogledov.find("<sup")])
                st_gledalcev += stevilo

print ("Skupno stevilo gledalcev znasa: %s milijonov" % st_gledalcev)

# <tr class="vevent" style="text-align:center;background:#F2F2F2">
# <table class="wikitable plainrowheaders wikiepisodetable" style="width:100%">
# https://en.wikipedia.org/wiki/Game_of_Thrones_(season_1)


