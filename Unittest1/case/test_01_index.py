import unittest
import time
from selenium import webdriver

class TestCaseIndex(unittest.TestCase):
    def test_01_search(self):
        driver=webdriver.Chrome("driver/chromedriver.exe")
        driver.get('http://118.24.255.132:19999/shopxo/')
        driver.find_element_by_id('search-input').send_keys('宝宝')
        driver.find_element_by_id('ai-topsearch').click()
        time.sleep(10)
        