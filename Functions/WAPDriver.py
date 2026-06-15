from selenium import webdriver
from typing import Text
class WAPDriver:
    ##初始化driver
    def __init__(self,Device: Text):
        mobile_emulation = {"deviceName": Device}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)
