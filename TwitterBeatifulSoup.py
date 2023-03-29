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
drive_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
browser=webdriver.Chrome(drive_path)
browser.get("https://www.google.com/search?q=tutkumuz+f1&oq=tut&aqs=chrome.0.69i59j69i57j0i131i433i512j69i61j69i60j69i61l2j69i65.1665j0j7&sourceid=chrome&ie=UTF-8")#sorun burada.get çalışmıyor
"""
yazi_girisi=browser.find_element(By.ID,"input")#selenium da classlar arasında boşluk var ise nokta koymak gerekiyor #browserden arama kutucuğunu seçme

yazi_girisi.send_keys("tutkumuz f1 twitter")#yazı girişi
time.sleep(2)#yazı girişinden sonra uyutuyor
yazi_girisi.send_keys(Keys.ENTER)
"""
tıkla=browser.find_element(By.CLASS_NAME,"haz7je")
tıkla.click()
