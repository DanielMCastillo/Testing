#Daniel Alejandro Morales Castillo
#22/09/2022 - Pruebas iterando en Google

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver_path =  "C:\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--start_maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(driver_path)



driver.get('https://google.com')

caja = driver.find_element(By.NAME, 'q')
caja.send_keys('interestelar'+Keys.RETURN)

time.sleep(5)

div_resultados = driver.find_element(By.ID, 'res')

elementos = div_resultados.find_elements(By.TAG_NAME, 'h3')

for item in elementos:
    if item.text != '':
        print(item.text)

driver.find_element(By.LINK_TEXT, 'Siguiente').click()

div_resultados = driver.find_element(By.ID, 'res')

elementos = div_resultados.find_elements(By.TAG_NAME, 'h3')

for item in elementos:
    if item.text != '':
        print(item.text)

while True:
    div_resultados = driver.find_element(By.ID,'res')
    elementos = div_resultados.find_elements(By.TAG_NAME, 'h3')
    
    for item in elementos:
        if item.text != '':
            print(item.text)
    try:
        driver.find_element(By.LINK_TEXT,'Siguiente').click()
    except:
        break
