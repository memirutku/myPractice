#hedef:amazonda teknik ayrıntı çekmek

from bs4 import BeautifulSoup
import requests

#best seller electronics
req=requests.get("https://www.amazon.com.tr/gp/bestsellers/electronics/ref=zg-bs_electronics_dw_sml")
soup=BeautifulSoup(req.content,"lxml") #parçalama işlemi

ürünler=soup.find_all("div",attrs={"class":"_cDEzb_grid-row_3Cywl"})
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#print(ürünler)

#tüm linkleri çekme işlemi
for ürün in ürünler:
    ürün_linkleri=ürün.find_all("div",attrs={"class":"zg-grid-general-faceout"})#arada boşluk varsa tüm classı olmıyorsun boşluktan sonrası alınıyor. Yoksa veri çekmez
    for i in ürün_linkleri:
        link=i.find("a",attrs={"class":"a-link-normal"}).get("href")
        link_basi="https://www.amazon.com.tr"
        link_tamami=link_basi+link
        #print(link_tamami)
        detay=requests.get(link_tamami,headers=header)
        #print(detay)#burada ki veri sayıysı ile ürünleri print ettiğimizde ki ürün sayısı aynı değil ise yanlılş veri çekinmi vardır bunu için ise incele den network e gidip son yapılan kendi işlemimizi seçip(ilk yapılan kendi işlemin oluyor)headersın en altından kendi user agentimizi seçmemiz lazım


        detay_soup = BeautifulSoup(detay.content,"lxml")
        teknik_detaylar=detay_soup.find_all("div",attrs={"class":"a-expander-extend-content"})#virgülden sonra ekstra detaylandırmak için özellik yazıyoruz

        for teknik in teknik_detaylar:
             detaylar=teknik.find_all("tr")#bütün <tr> leri almak istediğimizi söylüyoruz
             for i in detaylar:
                    try:
                        etiket=i.find("th",attrs={"class":"prodDetSectionEntry"}).text
                        deger=i.find("td",attrs={"class":"prodDetAttrValue"}).text
                        print(etiket," = ",deger)
                    except:
                        print("------------------")
