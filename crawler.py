import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.hareruyamtg.com/ja/products/search?category=1&cardset=263&page=1")
soup = BeautifulSoup(r.text,"html.parser")
price = soup.find_all("p", attrs={'class': 'itemDetail__price'})
name  = [soup.find_all("div", attrs={'class': 'itemData'})[i].find("a").text for i in range(len(price))]
for i in range(len(price)):
    print(name[i], price[i].text)
