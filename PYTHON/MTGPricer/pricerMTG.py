def avg(l):
    avg=sum(l)/len(l)
    return avg

def myround(x, base=1):
    return int(base * round(float(x)/base))

import json
import requests
import math

cardnameOrg="Tarmogoyf"
setnameOrg="Modern Masters"

#cardnameOrg="Godsend"
#setnameOrg="Journey into Nyx"

details=True
fxFrom="USD"
fxTo="SEK"

cardname=cardnameOrg.replace(" ","%20")
setname=setnameOrg.replace(" ","%20")

cfbAdress= "http://magictcgprices.appspot.com/api/cfb/price.json"
#ebayAdress= "http://magictcgprices.appspot.com/api/ebay/price.json"
tcgAdress= "http://magictcgprices.appspot.com/api/tcgplayer/price.json"
fxReq=('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (fxFrom,fxTo)

response = requests.get(fxReq)
data=json.loads(response.content)

fx=""
fx=data.get('v')

query="?cardname="+cardname+"&setname="+setname

cfb=cfbAdress+query
#ebay=ebayAdress+query
tcg=tcgAdress+query

response = requests.get(cfb)
data=json.loads(response.content)
cfbprice=0
cfbprice=float(data[0][1:])

response = requests.get(tcg)
data=json.loads(response.content)
tcgvec=[]

if details: print "="*35+"DETAILS"+"="*35
if details:print "Prices from tcg(USD):"
for strings in data:
    tcgprice=float(strings[1:])
    if details:print tcgprice
    tcgvec.append(tcgprice)

tcgavg=0




pricevec=[]
pricevec=tcgvec
pricevec.append(cfbprice)

avgvec=[tcgavg,cfbprice]

sekprice=avg(avgvec)*fx

roundprec=100
if sekprice<=100:roundprec=5
if 100<sekprice<=1000:roundprec=25

if details:
    print "\nTcgavg price(USD):"
    print tcgavg
    
    print "\nChannel fireball price(USD):"
    print cfbprice

    print "\nCurrency used for USD/SEK:"
    print fx

    print "\nRounding factor:"
    print roundprec
    
finalprice=myround(sekprice,roundprec)
priceinterval=[]
priceinterval=[myround(min(pricevec)*fx,roundprec),myround(max(pricevec)*fx,roundprec) ]

print "="*35+"OUTPUT"+"="*36
print "CARD: "+ cardnameOrg
print "SET: "+ setnameOrg

print "Price(SEK): " + str(finalprice)

print "\nPrice interval(SEK):"
print priceinterval

