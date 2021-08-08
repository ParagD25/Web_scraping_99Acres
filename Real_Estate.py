import requests
import pandas
from bs4 import BeautifulSoup

req=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Indore")
c=req.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})

prop_lst=[]
for items in all:
    dic={}
    try:
        dic['Price']=items.find("div",{"class","m-srp-card__price"}).text
    except:
        dic['Price']=None

    try:
        dic['Area']=items.find("div",{"class","m-srp-card__summary__info"}).text
    except:
        dic['Area']=None

    try:
        dic['Price per sqft']=items.find("div",{"class","m-srp-card__area"}).text
    except:
        dic['Price per sqft']='Not Available'

    try:    
        dic['Builder\'s Name']=items.find("div",{"class","m-srp-card__advertiser__name"}).text
    except:
        dic['Builder\'s Name']=None

    prop_lst.append(dic)

df=pandas.DataFrame(prop_lst)
df.to_csv("Property.csv")

