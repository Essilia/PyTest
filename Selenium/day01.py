from selenium import webdriver
from seleniumtools import find_element

#1、打开浏览器，实例化浏览器句柄/把柄

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

#2、打开网页
driver.get("http://test-hengyun.szzntech.com/dashboard/overview")
# #3、元素定位
# #id定位
# driver.find_element_by_id("kw").send_keys("nct")

# #xpath定位
# driver.find_element_by_xpath('//*[@id="su"]').click()

username=('xpath','//*[@id="root"]/div/div/div/div[2]/div[2]/div[1]/input')
password=('xpath','//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/span/input')
login=('xpath','//*[@id="root"]/div/div/div/div[2]/button')
find_element(driver,username).send_keys("admin")
find_element(driver,password).send_keys("123456")
find_element(driver,login).click()
