from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import time
import string
chromedriver=r"C:\Users\DHANU\Downloads\chromedriver" #your path of chromedriver
driver = webdriver.Chrome(chromedriver)
act = ActionChains(driver)

driver.get('https://flipkart.com/')

user = driver.find_element_by_class_name('_2zrpKA')
user.send_keys('#username in flipkart website')

passd=  driver.find_element_by_xpath("//input[@type='password']")
passd.send_keys('#password in flipkart website')


button = driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']")
button.click()

print('User Successfully Logined In')

time.sleep(5)

driver.get('https://www.flipkart.com/redmi-note-5-pro-black-64-gb/p/itmf2fc3xgmxnhpx?pid=MOBF28FTQPHUPX83&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_10&lid=LSTMOBF28FTQPHUPX83BUJJ2C&fm=SEARCH&iid=f4e84aa1-8a46-47aa-ba47-ec78a2190ca1.MOBF28FTQPHUPX83.SEARCH&ppt=Homepage&ppn=Homepage&ssid=4p59s19aq80000001543934963487&qH=286b43aac83aafdc')
print("product searched")

time.sleep(3)

buynow= driver.find_element_by_xpath("//button[@type='button']")
buynow.click()
print("buynow button clicked")

time.sleep(5)

countinue= driver.find_element_by_xpath("//button[@class='_2AkmmA _2Q4i61 _7UHT_c']")
countinue.click()
print("countinue button pressed")

time.sleep(3)
payment= driver.find_element_by_xpath("//button[@class='_2AkmmA _37mBT- _7UHT_c']")
payment.click()
print("payment countinue button clicked")

time.sleep(5)
paythroughphonepe= driver.find_element_by_id('paySubmitButton')
paythroughphonepe.click()
print("waiting for confirmation through phonepe")

