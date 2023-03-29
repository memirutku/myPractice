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
time.sleep(2)#yazı girişinden sonra uyutuyor
yazi_girisi.send_keys(Keys.ENTER)

tıkla=browser.find_element(By.CLASS_NAME,"haz7je")
tıkla.click()








time.sleep(9999)

#time sleep olayı ney onu sor