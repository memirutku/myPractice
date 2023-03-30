#hedef: twitterden veri elde etmek
#veri çekme kısmında selenium kullanıcaz request yerine
#beatifulsoup ile parçalayacağız
#request ile aldığımız zaman sayfanın bazı kısımları gelmiyor ve sayfayı scroll etmemiz gerekiyor o yüzden selenium kullanıyoruz
#verimizi csv ya  da excel dosyasına kaydedicez
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd

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

#pop up kapatmak için
pop_up=browser.find_element(By.CLASS_NAME,"r-4qtqp9.r-yyyyoo.r-z80fyv.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-19wmn03")
pop_up.click()


##hazır kod googleden scrollamak için (aşağı doğru inme)
lastHeight=browser.execute_script("return document.body.scrollHeight")
i=0
while i<1: # sonsuza kadar gitmesini engellemek için
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
    newHeight=browser.execute_script("return document.body.scrollHeight")
    if newHeight==lastHeight:
        break
    else:
        lastHeight=newHeight
    i+=1
##


page_source=browser.page_source #browser değişkeniyle girdiğimiz için .page_source sayfanın kaynağını getiriyor
soup = BeautifulSoup(page_source,"html.parser")#normalde beatifulSoup da .content koyuyoruz ama browser.page_source ile o işlemi yapmış oluyoruz zaten
#print(soup)


tweetler=soup.find_all("div",attrs={"data-testid":"cellInnerDiv"})#bütün twitleri almak için find_all diyoruz yoksa sadece find #ilk kısımda neyden ayıracağımızı(div olan kısım) #attrs kısmında ayırt edici özelliğini yazıyoruz


for tweet in tweetler:
    twit=(tweet.find("div",attrs={"class":"css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}).text)#seleniumda boşluk yerine nokta koyarak ile alabiliyorken. beatifulsoupda böyle bir şey yok.
    begeni=(tweet.find("div",attrs={"data-testid":"like"}).text)
    yorum=(tweet.find("div",attrs={"data-testid":"reply"}).text)
    retweet=(tweet.find("div",attrs={"data-testid":"retweet"}).text)
    print(f"tweet: {twit}" )
    print(f"begeni: {begeni}")
    print(f"yorum: {yorum}")
    print(f"retweet: {retweet}")







print("for döngüsü bitti")
time.sleep(99999)



#sorular
#neden chrome.exe yerine chromedriver.exe
#time sleep olayı olmadan da açık kalabiliyor mu
#en işe yarayacak div deneme yanılma ile mi bulunacak yoksa kısa bir yolu var mı
#amazonda boşluğu sildirdi bunda sildirmedi nedenini sor
#çıktı da boşluklardan nasıl kurtulabilirim
# hata veriyor o da sorulmalı sisteme bağlı bir aygıt çalışmıyor ile ilgili