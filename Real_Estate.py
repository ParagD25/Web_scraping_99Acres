import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.99acres.com/search/property/buy/residential-all/indore?search_type=QS&refSection=GNB&search_location=HP&lstAcn=HP_R&lstAcnId=0&src=CLUSTER&preference=S&selected_tab=1&city=142&res_com=R&property_type=R&isvoicesearch=N&keyword=indore&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null")
c=req.content
soup=BeautifulSoup(c,"html.parser")
