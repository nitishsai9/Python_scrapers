from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ur
import requests

URL='https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page=requests.get(URL,headers=headers)
soup=bs(page.content,'html.parser')
containers=soup.find_all("div",{"class":"_3O0U0u"})
print(len(containers))
# print(bs.prettify(containers[0]))
container=containers[0]
price=container.find_all("div",{"class":"col col-5-12 _2o7WAb"})
# print(len(price))
# print(price[0].text)
ratings=container.find_all("div",{"class":"niH0FQ"})
# 
fname="fip.csv"
f=open(fname,"w")
headers="p_name , price,Rating \n"
f.write(headers)
for container in containers:
    
    p_name=container.div.img["alt"]
    pr_c=container.find_all("div",{"class":"col col-5-12 _2o7WAb"})
    price=pr_c[0].text.strip()
    r_c=container.find_all("div",{"class":"niH0FQ"})
    ratings=r_c[0].text

    p_c= ''.join(price.split(','))

    r_c1=price.split('₹')

    addrs="Rs"+r_c1[1]
    split_p=addrs.split('E')
    finalPrice=split_p[0]

    s_r=ratings.split(" ")
    f_r=s_r[0]
    print(p_name.replace("," , "|")+finalPrice+','+ f_r+"\n")
    f.write(p_name.replace("," , "|")+finalPrice+','+ f_r+"\n")
f.close()

 