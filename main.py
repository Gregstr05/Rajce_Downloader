import urllib.request
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(input("URL of a first photo: "))

sleep(25)

print('Still trying and not failing')

i = 0

for i in range(687):
    print(i)
    try:
        print("tried xd")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "detail-image"))
        )
    finally:
        img = driver.find_element(By.ID, 'detail-image')
        src = img.get_attribute('src')

        urllib.request.urlretrieve(src, f"./images/image_{i}.png")

        sleep(.1)

        next_photo = driver.find_element(By.ID, 'show-next-medium')
        next_photo.click()
        i += 1

print("Done :)")

sleep(69)

driver.quit()
