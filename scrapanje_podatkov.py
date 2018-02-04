from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

class Oseba:
    def __init__(self, ime, priimek, email, kraj):
        self.ime = ime
        self.priimek = priimek
        self.email = email
        self.kraj = kraj

MAIN_URL = "https://scrapebook22.appspot.com/"

webpage = urlopen(MAIN_URL).read()
nice_webpage = BeautifulSoup(webpage) # stran se transformira v bolj berljivo in lazje upravljivo


podatki = nice_webpage.tbody.findAll("tr") # ukaz najde prvi tbody in izpise vse tr znacke v listo
#print podatki[0]
#spodaj je prikazano kaj dobimo z izpisom podatki[0]
#<tr>
#<td>John</td>
#<td>Hillnob</td>
#<td>52</td>
#<td>Oxford</td>
#<td><a href="/person/5066549580791808">See full profile</a></td>
#</tr>

imena = []
priimki = []
kraji = []

for item in podatki:
    item = str(item)
    item = item.split("\n") # locimo posamezne posamezen element v podatkih po novih vrstah v novo listo
    ime = item[1]
    priimek = item[2]
    kraj = item[4]
    ime = ime[ime.find(">")+1:ime.find("</")] # izpise ime
    priimek = priimek[priimek.find(">") + 1:priimek.find("</")]
    kraj = kraj[kraj.find(">") + 1:kraj.find("</")]
    imena.append(ime)
    priimki.append(priimek)
    kraji.append(kraj)
#print imena
#print priimki
#print kraji

emaili = []

linki = nice_webpage.findAll("a") # najde vse povezave s kljucem a
for link in linki:
    if link.string == "See full profile": # izloci povezave a ki nimajo tega stringa
        personal_page = BeautifulSoup(urlopen(MAIN_URL + link["href"]).read()) # odpre novo stran
        email = personal_page.find("span", {"class": "email"}).string # izloci email naslov po classu email v spanu
        emaili.append(email)
#print emaili


posamezniki = []
for i in range(len(imena)):
    posameznik = Oseba(imena[i], priimki[i], emaili[i], kraji[i]) # podatke transformiramo v class
    posamezniki.append(posameznik)

# Ustvarimo novo datoteko

csv_file = open("osebe.csv", "w")

for osebek in posamezniki:
    csv_file.write(osebek.ime + " " + osebek.priimek + "," + osebek.email + "," + osebek.kraj + "\n")

csv_file.close()


