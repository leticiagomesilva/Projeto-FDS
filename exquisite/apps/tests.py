from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options)

class Test(LiveServerTestCase):

    def test_criar_perguntas(self):
        
        driver.get('https://exquisite-app.azurewebsites.net/')
        
        for i in range(1,5):
            register = driver.find_element(By.NAME,'Criar Perguntas')
            register.click()


            materia = driver.find_element(By.ID,'materia')
            titulo = driver.find_element(By.ID,'titulo')
            pergunta = driver.find_element(By.ID,'pergunta')
            resposta = driver.find_element(By.ID,'resposta')

            materia.send_keys('Matemática')
            titulo.send_keys('Soma')
            pergunta.send_keys('4 + 6')
            resposta.send_keys('10')

            cadastrar = driver.find_element(By.NAME,'Cadastrar Pergunta')
            cadastrar.click()


            cadastrar.send_keys(Keys.RETURN)