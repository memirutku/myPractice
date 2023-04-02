from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd

#veri çekme
#request
#selenium

#parçalama
#beatiful soup ile

drive_path="C:\Amazon Games\chromedriver.exe"#chrome driver olmak zorunda o da ekstra indiriliyor
browser=webdriver.Chrome(drive_path)
browser.get("https://www.google.com/")


yazi_girisi=browser.find_element(By.CLASS_NAME,"gLFyf")
yazi_girisi.send_keys("btk akademi twitter")
yazi_girisi.send_keys(Keys.ENTER)

tıkla=browser.find_element(By.CLASS_NAME,"haz7je")
tıkla.click()




time.sleep(30)#pop up uzun sürede açıldığı için burada bekliyoruz

#pop up kapatmak için #try except eklenebilir buraya
pop_up=browser.find_element(By.CLASS_NAME,"r-4qtqp9.r-yyyyoo.r-z80fyv.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-19wmn03")
pop_up.click()






page_source=browser.page_source
soup = BeautifulSoup(page_source,"html.parser")

tweetler=soup.find_all("div",attrs={"data-testid":"cellInnerDiv"})




for x in tweetler:
 tweet=x.find("div",attrs={"data-testid":"tweetText"}).text

 print(tweet)

print("Kodun sonu")

time.sleep(31313131)

