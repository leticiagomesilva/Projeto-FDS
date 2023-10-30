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
print(f"\nTeste de Acessar Ranking no site {driver.title}")

try:
    sleep(2)
    erro = "clicar ranking"
    acessar_ranking = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "listagem_ranking")))
    acessar_ranking.click()

    sleep(4)
    erro = "printar ranking"
    ranking = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "# Nome Sobrenome Pontos" in ranking.text:
        print("Ranking acessado com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()