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
print(f"\nTeste de Responder Perguntas no site {driver.title}")

try:
    sleep(3)
    erro = "clicar acessar perguntas"
    acessar_perguntas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "listagem_perguntas")))
    acessar_perguntas.click()

    sleep(2)
    erro = "clicar soma"
    soma = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/a")))
    soma.click()

    sleep(2)
    erro = "digitar resposta errada"
    resposta_errada = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resposta")))
    resposta_errada.clear()
    resposta_errada.send_keys("5")
    
    sleep(2)
    erro = "clicar responder"
    cadastrar_pergunta = driver.find_element(By.NAME, "responder")
    cadastrar_pergunta.click()

    sleep(2)
    erro = "digitar resposta correta"
    resposta_corret = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resposta")))
    resposta_corret.clear()
    resposta_corret.send_keys("4")

    sleep(2)
    erro = "clicar responder"
    cadastrar_pergunta = driver.find_element(By.NAME, "responder")
    cadastrar_pergunta.click()
    
    sleep(4)
    erro = "printar confirmação"
    confirmacao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "center")))
    
    if "Parabéns! Você acertou essa pergunta" in confirmacao.text:
        print("Pergunta respondida com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()