import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Indore")
c=req.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})
# print(all[0].find("div",{"class":"m-srp-card__price"}).text)
for items in all:
    try:
        print(items.find("div",{"class","m-srp-card__price"}).text)
    except:
        print(None)
    try:
        print(items.find("div",{"class","m-srp-card__summary__info"}).text)
    except:
        print(None)
    try:    
        print(items.find("div",{"class","m-srp-card__advertiser__name"}).text)
    except:
        print(None)
    print()