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
    sleep(1)
    erro = "clicar criar perguntas"
    criar_perguntas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "criar_perguntas")))
    criar_perguntas.click()
    
    sleep(1)
    erro = "digitar materia"
    materia = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "materia")))
    materia.clear()
    materia.send_keys("Matemática")
    
    sleep(1)
    erro = "digitar titulo"
    titulo = driver.find_element(By.NAME, "titulo")
    titulo.clear()
    titulo.send_keys("Soma")
    
    sleep(1)
    erro = "digitar pergunta"
    pergunta = driver.find_element(By.NAME, "pergunta")
    pergunta.clear()
    pergunta.send_keys("2+2")
    
    sleep(1)
    erro = "digitar resposta"
    resposta = driver.find_element(By.NAME, "resposta")
    resposta.clear()
    resposta.send_keys("4")
    
    sleep(1)
    erro = "clicar cadastrar pergunta"
    cadastrar_pergunta = driver.find_element(By.NAME, "cadastrar_pergunta")
    cadastrar_pergunta.click()
    
    sleep(2)
    erro = "printar perguntas"
    perguntas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "Matemática Soma 2+2" in perguntas.text:
        print("Pergunta criada com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()