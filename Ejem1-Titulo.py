from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
#ubicacion del driver.
driver = webdriver.Chrome(executable_path='C:\\Users\\x\\Documents\\chromedriver.exe')

#pagina a trabajar
driver.get("https://demoqa.com/")

print ("TITULO DE PAGINA: ",driver.title)
driver.close