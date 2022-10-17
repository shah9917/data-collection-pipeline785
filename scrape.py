from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import time 


driver = Chrome(ChromeDriverManager().install())
#driver.get("https://uk.trustpilot.com/")

class Scraper:
    def __init__(self, website):
        self.website = website
    
    def get_website(self):
        return driver.get(self.website)

    def close(self):
        driver.quit()

    def ignore_cookie(self):
        try:
            driver.switch_to.frame('onetrust-consent-sdk')
            ignore_cookies = driver.find_element(by = By.XPATH, value='//*[@id="onetrust-rehect-all-handler"]')
            ignore_cookies.click()
        except:
            pass

reviews = Scraper("https://uk.trustpilot.com/")
reviews.get_website()
time.sleep(2)
reviews.ignore_cookie()
time.sleep(2)
reviews.close()

