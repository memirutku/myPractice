#hedef: twitterden veri elde etmek
#veri çekme kısmında selenium kullanıcaz request yerine
#beautifulSoup ile parçalayacağız
#request ile aldığımız zaman sayfanın bazı kısımları gelmiyor ve sayfayı scroll etmemiz gerekiyor o yüzden selenium kullanıyoruz
#verimizi csv ya  da excel dosyasına kaydedicez
#notlar: beautifulSoup da genellikle request kullanılır veriyi çekmek için scroll işlemi olduğu için seleniumla daha kolay
#beautifulsoup localde yaptığı için daha hızlı seleniumla parçalamaktan
#request ile çekip beatifulsoup ile parçalamak
#beatifulsoup daha hızlı parçalamada seleniuma göre




from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd

def veri_cek():
    sayfa=int(input("scroll sayısını girin= "))#kaç scroll yapacağımızı verisi kullanıcıdan

    #google yi açma kısmı
    drive_path="C:\Amazon Games\chromedriver.exe"#chrome driver olmak zorunda o da ekstra indiriliyor
    browser=webdriver.Chrome(drive_path)
    browser.get("https://www.google.com/")


    yazi_girisi=browser.find_element(By.CLASS_NAME,"gLFyf")#selenium da classlar arasında boşluk var ise nokta koymak gerekiyor #browserden arama kutucuğunu seçme

    yazi_girisi.send_keys("tutkumuz f1 twitter")#yazı girişi
    #time.sleep(2)#yazı girişinden sonra uyutuyor
    yazi_girisi.send_keys(Keys.ENTER)#entere basma

    tıkla=browser.find_element(By.CLASS_NAME,"haz7je")#çıkan ilk linki seçme
    tıkla.click()#linke basma

    time.sleep(20)#pop up uzun sürede açıldığı için burada bekliyoruz

    #pop up kapatmak için #try except eklenebilir buraya
    pop_up=browser.find_element(By.CLASS_NAME,"r-4qtqp9.r-yyyyoo.r-z80fyv.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-19wmn03")
    pop_up.click()

    #csv dosya oluşturma
    file=open("tweetler.csv","w",encoding="utf-8")#yolu vermez isen python dosyası neredeyse orada kurulacaktır
    writer=csv.writer(file)
    writer.writerow(["tweetler","beğeni_sayısı","yorum_sayısı","retweet_sayısı"])#başlık oluşturuyoruz



    a=0
    while a<(sayfa+1):#bunu yapma nedeni de her scrolldan sonra veriyi çekebilme

        page_source=browser.page_source #browser değişkeniyle girdiğimiz için .page_source sayfanın kaynağını getiriyor
        soup = BeautifulSoup(page_source,"html.parser")#normalde beatifulSoup da .content koyuyoruz ama browser.page_source ile o işlemi yapmış oluyoruz zaten
        #print(soup)


        tweetler=soup.find_all("div",attrs={"data-testid":"cellInnerDiv"})#bütün twitleri almak için find_all diyoruz yoksa sadece find #ilk kısımda neyden ayıracağımızı(div olan kısım) #attrs kısmında ayırt edici özelliğini yazıyoruz


        for tweet in tweetler:
            try:
                twit=(tweet.find("div",attrs={"class":"css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}).text)#seleniumda boşluk yerine nokta koyarak ile alabiliyorken. beatifulsoupda böyle bir şey yok.
                begeni=(tweet.find("div",attrs={"data-testid":"like"}).text)
                yorum=(tweet.find("div",attrs={"data-testid":"reply"}).text)
                retweet=(tweet.find("div",attrs={"data-testid":"retweet"}).text)
                print(f"tweet: {twit}" )
                print(f"begeni: {begeni}")
                print(f"yorum: {yorum}")
                print(f"retweet: {retweet}")
                writer.writerow([twit,begeni,yorum,retweet])#sıralama önemli başlıklar ile aynı olması için
            except:
                print("***")

        ##scroll kodu googleden
        lastHeight=browser.execute_script("return document.body.scrollHeight")

            #   scroll çok fazla aşağı doğru gidiyor scroll kısmında
        i=0
        while i<(sayfa): # sonsuza kadar gitmesini engellemek için
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(5)
            newHeight=browser.execute_script("return document.body.scrollHeight")
            if newHeight==lastHeight:
                break
            else:
                lastHeight=newHeight
            i+=1
            ##
        a+=1
    #time.sleep(99999)



veri_cek()

pandas_csv=pd.read_csv("tweetler.csv")#ilk çıktı hatalı olabiliyor pandas onu düzeltiyor
pandas_csv.to_excel("tweetler_.excel.xlsx")#düzeltilmiş halini de excel e çeviriyoruz


print("for döngüsü bitti")

##csv dosyasına yazılmıyor yazılmadığı için excel e çevirilmiyor





#elindeki twit sayısına bak ona göre while loopu


#sorular
#neden chrome.exe yerine chromedriver.exe
#time sleep olayı olmadan da açık kalabiliyor mu
#en işe yarayacak div deneme yanılma ile mi bulunacak yoksa kısa bir yolu var mı
#amazonda boşluğu sildirdi bunda sildirmedi nedenini sor
#çıktı da boşluklardan nasıl kurtulabilirim
# hata veriyor o da sorulmalı sisteme bağlı bir aygıt çalışmıyor ile ilgili
#selenium kullanmadan sadece beatifulsoup ve .request ile çekme şansımız var mı
#twitterBeautifulsoup ve amazon beautifulsoupvar