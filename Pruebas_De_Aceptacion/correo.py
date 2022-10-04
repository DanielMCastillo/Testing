from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from contra import *

driver_path =  "C:\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--start_maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(driver_path)



driver.get('https://outlook.com')

caja = driver.find_element(By.LINK_TEXT, 'Iniciar sesión').click()
caja = driver.find_element(By.NAME, 'loginfmt').send_keys(correo)
caja = driver.find_element(By.ID, 'idSIButton9').click()

time.sleep(2)

caja = driver.find_element(By.NAME, 'passwd').send_keys(contra)
time.sleep(2)

caja = driver.find_element(By.ID, 'idSIButton9').click()
time.sleep(1)


caja = driver.find_element(By.ID, 'idBtn_Back').click()
time.sleep(1)


caja = driver.find_element(By.CLASS_NAME, 'NtlqS NQ_Mj VuLGw').click()
time.sleep(1)

caja = driver.find_element(By.TITLE, 'Bandeja de entrada').click()
time.sleep(1)

caja = driver.find_element(By.TITLE, 'Correo no deseado').click()
time.sleep(1)

caja = driver.find_element(By.NAME, 'Vaciar carpeta').click()
time.sleep(1)

caja = driver.find_element(By.ID, 'id_533').click()




#extraer el asunto y remitente de los primeros 100
#eliminar la bandeja de spam
#->correo no deseado -> vaciar carpeta