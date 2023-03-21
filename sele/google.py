from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request



chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=chrome_option)
# chrome_options=chrome_option
driver.get('https://www.google.com/imghp?hl=en&ogbl')

element = driver.find_element(By.NAME, 'q')
element.send_keys("square face")
element.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
        except:
            break
    last_height = new_height



count = 0
images= driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
for image in images:
	# try:
		driver.find_element(By.TAG_NAME,"body").send_keys(Keys.HOME)
		download = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")[count].get_attribute("src")
		urllib.request.urlretrieve(download,str(count)+".jpg")
		count = count +1
		time.sleep(0.2)
		driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
	# except:
	# 	pass
driver.close()

