from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Bsoup

#Beautifulsoup would parse the html text in a page while urllib would grab the page itself.

#Web scrapping graphics cards of newegg.com(amazon for hardware electronics)
target_url = 'https://www.newegg.com/global/ie/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=samsung+s8+plus&ignorear=0&N=-1&isNodeId=1'
uClient = uReq(target_url)#open the connection,grab the webpage and download it
page_html = uClient.read()
uClient.close()
#html parsing
page_soup = Bsoup(page_html,"html.parser")#first argument html page and second argument is what to parse is it html or xml page etc

#converting all the phone (samsung 8) models data to a csv file.

#next step is to inspect the element of a page,i.e, model and go to the html root/child thats holding the entire container for that phone model.
#Once one model is taken care of then we can loop through all other remaining ones,similarly.

#grabs each product
containers = page_soup.find_all("div",{"class":"item-container"})#feeding an object  as second parameter

filename = "mobile_product.csv"
f = open(filename,"w")
headers = "brand, Operating System, Price\n"
f.write(headers)

for container in containers:
    model = container.a.img["alt"].strip()

    feature_container = container.findAll("ul",{"class":"item-features"})
    operating_system = feature_container[0].li.text[18:].strip()

    price_container = container.findAll("li", {"class": "price-current"})
    price_model = price_container[0].text.strip()

    f.write(model.replace(",","|") + "," + operating_system.replace(",","|") + "," + price_model.replace(",","|"))
f.close()


