import requests
from bs4 import BeautifulSoup



for ii in range(300):
    f = open("crawl_result.dat","a")
    r = requests.get("https://www.hareruyamtg.com/ja/products/search?category=1&cardset="+str(ii)+"&page=1")
    soup = BeautifulSoup(r.text,"html.parser")
    price = soup.find_all("p", attrs={'class': 'itemDetail__price'})
    name  = [soup.find_all("div", attrs={'class': 'itemData'})[i].find("a").text for i in range(len(price))]
    for i in range(len(price)):
        f.write(name[i]+price[i].text)
    numofgoods = int(soup.find("p",attrs={"class":"count_number"}).text)
    for j in range(2,int(numofgoods//60+1)):
        print("ii=",ii,"j=",j)
        r = requests.get("https://www.hareruyamtg.com/ja/products/search?category=1&cardset="+str(ii)+"&page="+str(j))
        soup = BeautifulSoup(r.text,"html.parser")
        price = soup.find_all("p", attrs={'class': 'itemDetail__price'})
        name  = [soup.find_all("div", attrs={'class': 'itemData'})[i].find("a").text for i in range(len(price))]
        for i in range(len(price)):
            f.write(name[i]+price[i].text)
    f.close()

