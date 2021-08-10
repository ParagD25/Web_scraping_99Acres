import requests
import pandas
from bs4 import BeautifulSoup

req=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Indore")
cont=req.content
soup=BeautifulSoup(cont,"html.parser")
all_data=soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})

prop_lst=[]
for items in all_data:
    dic={}
    #Flat Price
    try:
        dic['Price']=items.find("div",{"class","m-srp-card__price"}).text
    except:
        dic['Price']=None

    #Flat Area
    try:
        dic['Area']=items.find("div",{"class","m-srp-card__summary__info"}).text
    except:
        dic['Area']=None

    #Price of Flat per sqft
    try:
        dic['Price per sqft']=items.find("div",{"class","m-srp-card__area"}).text
    except:
        dic['Price per sqft']='Not Available'

    #Type of furnishing
    for col_data in items.find_all("div",{"class":"m-srp-card__summary js-collapse__content"}):
        for feat_title,feat_info in zip(col_data.find_all("div",{"class":"m-srp-card__summary__title"}),col_data.find_all("div",{"class":"m-srp-card__summary__info"})):
            if "furnishing" in feat_title.text:
                dic['Furnishing']=feat_info.text
            if "status" in feat_title.text:
                dic['Status']=feat_info.text
    #Name Of Builder/Seller
    try:    
        dic['Builder\'s Name']=items.find("div",{"class","m-srp-card__advertiser__name"}).text
    except:
        dic['Builder\'s Name']=None

    prop_lst.append(dic)

df=pandas.DataFrame(prop_lst)
df.to_csv("Property.csv")

