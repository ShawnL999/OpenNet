from selenium import webdriver

class Screenshot:

    def ExportScreenshot(driver: webdriver):
        driver.get_screenshot_as_file("imag.png")