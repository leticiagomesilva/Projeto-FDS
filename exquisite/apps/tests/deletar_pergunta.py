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
print(f"\nTeste de Excluir Perguntas no site {driver.title}")

try:
    sleep(2)
    erro = "clicar acessar perguntas"
    acessar_perguntas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "listagem_perguntas")))
    acessar_perguntas.click()

    sleep(3)
    erro = "clicar excluir perguntas"
    excluir_pergunta = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "excluir_pergunta")))
    excluir_pergunta.click()
    
    sleep(2)
    erro = "digitar titulo"
    titulo = driver.find_element(By.NAME, "titulo")
    titulo.clear()
    titulo.send_keys("Descobridor da Gravidade")
    
    sleep(2)
    erro = "clicar excluir"
    excluir = driver.find_element(By.NAME, "excluir")
    excluir.click()
    
    sleep(4)
    erro = "printar perguntas"
    perguntas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "Física Descobridor da Gravidade Quem foi o cientista famoso que descobriu a gravidade?" not in perguntas.text:
        print("Pergunta excluida com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()