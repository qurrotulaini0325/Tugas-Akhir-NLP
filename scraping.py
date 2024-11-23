from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scroll(height):
    driver.execute_script(f"window.scrollTo(0, {height});")

option = webdriver.ChromeOptions()
servicePath = Service('D:\CodingStuff\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=servicePath, options=option)

driver.get("https://www.tokopedia.com/")
driver.maximize_window()
print("Browser opened successfully.")

time.sleep(3)

searchbar = driver.find_element(By.CLASS_NAME, "css-3017qm")
searchbar.send_keys("Mystery Box", Keys.ENTER)
print("Search query submitted.")

time.sleep(10)
scroll(300)

product = driver.find_element(By.XPATH, "//span[text()='Mistery Box Dapat hp - unboxing misteri box misterius / misteri dapat']")
product.click()
print("Product clicked.")
time.sleep(3)

scroll(1500)
print("Scrolled to comments section.")
time.sleep(10)

comments = driver.find_elements(By.XPATH, "//span[@data-testid='lblItemUlasan']")
dataComment = [comment.text for comment in comments]

print("\nComments found:")
for num, comment in enumerate(dataComment, start=1):
    print(f"{num}. {comment}")

time.sleep(3)

driver.quit()
