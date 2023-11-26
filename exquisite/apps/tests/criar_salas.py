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
    erro = "clicar criar salas"
    criar_salas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "criar_salas")))
    criar_salas.click()
    
    sleep(1)
    erro = "digitar titulo"
    titulo = driver.find_element(By.NAME, "titulo_sala")
    titulo.clear()
    titulo.send_keys("Garagino")
    
    sleep(1)
    erro = "digitar materia"
    materia = driver.find_element(By.NAME, "preferencia")
    materia.clear()
    materia.send_keys("Computação Física")
    
    sleep(2)
    erro = "clicar cadastrar sala"
    cadastrar_pergunta = driver.find_element(By.NAME, "cadastrar_sala")
    cadastrar_pergunta.click()
    
    sleep(4)
    erro = "printar salas"
    salas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "Garagino Computação Física" in salas.text:
        print("Sala criada com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()