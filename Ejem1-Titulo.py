from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

#ubicacion del driver.
driver = webdriver.Chrome(executable_path='C:\\Users\\x\\Documents\\chromedriver.exe')

#pagina a trabajar
driver.get("https://demoqa.com/")

#ELIMINAR REGISTRO DE ERRORES EN CONSOLA


print ("TITULO DE PAGINA: ",driver.title)
driver.close