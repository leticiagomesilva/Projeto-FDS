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
print(f"\nTeste de Criar Perguntas no site {driver.title}")

try:
    sleep(2)
    erro = "clicar metas"
    acessar_meta = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "acessar_meta")))
    acessar_meta.click()

    sleep(3)
    erro = "clicar atualizar meta"
    atualizar_meta = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "atualizar_meta")))
    atualizar_meta.click()

    sleep(2)
    erro = "clicar 21 perguntas"
    perguntas_21 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "21 perguntas")))
    perguntas_21.click()
    
    sleep(2)
    erro = "clicar enviar meta"
    enviar_meta = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "enviar_meta")))
    enviar_meta.click()
    
    sleep(4)
    erro = "printar meta"
    meta = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "center")))
    
    if "21 perguntas" in meta.text:
        print("Meta atualizada com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()