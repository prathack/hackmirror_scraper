import pythonwhois as p
from bs4 import BeautifulSoup as b
import lxml
import urllib.request as urllib
from urllib.parse import urlparse
from termcolor import colored
from colorama import *
init()
print(Fore.YELLOW+""" Options:
    
                    1 -> onhold_attacks
                    2 -> special_attacks
                    3 -> archive_attacks
    """)
    
options = ['onhold','special','attacks']
option = options[int(input("Enter option number: "))-1]
for k in range(1,11):
    print(Fore.WHITE+"Extracting from Page: "+str(k))
    site = 'http://www.hack-mirror.com/'+option+'_'+str(k)+'.html'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.Request(site,headers=hdr)
    url = urllib.urlopen(req).read()
    html = b(url,"lxml")
    rows = html.findAll('tr')
    for i in rows[1:21]:
        tds = i.findAll('td')
        if 'www.' in tds[8].text:
            website = tds[8].text[4:]
        else:
            website = tds[8].text
        try:
            name = tds[1].text
        except:
            name = "None"
        try:
            team = tds[2].text
        except:
            team = "None"
        newUrl = ''
        for u in website:
            if '/' not in u:
                newUrl = newUrl+str(u)
            else:
                break
        try:
            d = p.get_whois(str(newUrl))
            print(Fore.GREEN+'Email ID for '+str(newUrl)+': '+d['contacts']['registrant']['email'])
        except:
            print(Fore.RED+"No Email for "+str(newUrl))
