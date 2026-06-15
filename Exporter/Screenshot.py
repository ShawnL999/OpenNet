from selenium import webdriver

class Screenshot:
    ## 輸出截圖
    def ExportScreenshot(driver: webdriver):
        driver.get_screenshot_as_file("imag.png")