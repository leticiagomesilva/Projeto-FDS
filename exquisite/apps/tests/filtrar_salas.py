from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

PATH = webdriver.ChromeService(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=PATH)

driver.get("http://127.0.0.1:8000/")
print(f"\nTeste de Criar Salas no site {driver.title}")

try:
    sleep(2)
    erro = "clicar salas"
    salas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "salas")))
    salas.click()

    sleep(2)
    erro = "clicar acessar salas"
    acessar_salas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "acessar_salas")))
    acessar_salas.click()

    sleep(3)
    erro = "clicar filtrar salas"
    filtrar_salas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "filtrar_salas")))
    filtrar_salas.click()
    
    sleep(1)
    erro = "digitar materia"
    materia = driver.find_element(By.NAME, "filtro_materia")
    materia.clear()
    materia.send_keys("Matemática")
    
    sleep(2)
    erro = "clicar acessar salas2"
    acessar_salas2 = driver.find_element(By.NAME, "acessar_salas")
    acessar_salas2.click()
    
    sleep(4)
    erro = "printar salas"
    salas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "Matemática" in salas.text:
        print("Salas filtradas com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()