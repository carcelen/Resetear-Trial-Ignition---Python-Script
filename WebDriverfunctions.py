""" Aut: DCL. 28/06/2020
    Funciones para resetear trial de Ignition. Necesario modulo selenium (webdriver).
    En este codigo se usa firefox como webdriver. Necesario añadir geckodriver.exe
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#Definimos la clase WebDriverIgnition
class WebDriverIgnition():
    #Funcion para incializar el webdriver en Firefox
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}
    #Funcion para cerrar el webdriver
    def teardown_method(self, method):
        self.driver.quit()
    #Funcion para resetear la trial de Ignition.
    def reset_trial(self,url,user,password):
        #Va a la pagina de igniton
        self.driver.get(url)
        #Espera implicita de 10ms para que carguen todos los elementos.
        self.driver.implicitly_wait(10)
        #Busca el elemento rest-trial-anchor y haz click
        self.driver.find_element(By.ID, "reset-trial-anchor").click()
        #Busca el elemento id1 y haz click (Para loguearse)
        self.driver.find_element(By.ID, "id1").click()
        #Inserta el usario
        self.driver.find_element(By.ID, "id1").send_keys(user)
        #Inserta las claves
        self.driver.find_element(By.NAME, "password").send_keys(password)
        #Click en aceptar el login.
        self.driver.find_element(By.ID, "id3").click()
        #Click en el elemento de restar trial.
        self.driver.find_element(By.ID, "reset-trial-anchor").click()


