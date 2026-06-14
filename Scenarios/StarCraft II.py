from Functions.WAPDriver import WAPDriver
from Exporter.Screenshot import Screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import time

queryKey = "StarCraft II"
Trytimes = 5
Device = "iPhone 14 Pro Max"

Wap = WAPDriver(Device)
Wap.driver.get("https://m.twitch.tv/")
btn_browse = Wap.driver.find_element(By.XPATH, "//*[contains(@id,'root')]/div[2]/a[2]")
btn_browse.click()
time.sleep(3)
txt_query = Wap.driver.find_element(By.XPATH, "//*[contains(@id,'twilight-sticky-header-root')]/div/div/div/div/input")
txt_query.click()
txt_query.send_keys(queryKey, Keys.ENTER)
time.sleep(3)
for i in range(Trytimes):
    Wap.driver.execute_script("window.scrollBy(0, 200);")
    Wap.driver.execute_script("window.scrollBy(0, 200);")
    #ActionChains(Wap.driver).scroll_by_amount(0, 200).perform()
    div_streamer = Wap.driver.find_elements(By.CLASS_NAME, "eMycWd")
    if len(div_streamer)>0:
        index = random.randint(0, len(div_streamer)-1)
        #actions = ActionChains(Wap.driver)
        #actions.scroll_to_element(div_streamer[index]).perform()
        #Wap.driver.scroll_to_element_with_offset(div_streamer[index])
        Wap.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", div_streamer[index])
        div_streamer[index].click()
        break


    else:
        if i==Trytimes-1:
            print("無頻道")
            break
        Wap.driver.refresh()
        time.sleep(3)

time.sleep(5)

while Wap.driver.execute_script("return document.readyState;") != "complete":
    time.sleep(0.5)

div_streaming = Wap.driver.find_element(By.CLASS_NAME, "video-player__default-player")
for i in range(Trytimes):
    if div_streaming.is_displayed():
        Screenshot.ExportScreenshot(Wap.driver)
        break
    else:
        if i==Trytimes-1:
            print("等待過久")
            break
        time.sleep(3)

Wap.driver.quit()