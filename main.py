""" Aut: DCL. 28/06/2020
    Script para resetear la trial de Ignition. Necesario modulo selenium (webdriver).
"""
import WebDriverfunctions
#Parametros de configuracion de ignition:
#URL:
sUrlIgniton = "http://localhost:8088/web/home?0"
#Credenciales para login
sUser = "admin"
sPassword = "80ds80nmWF"

Ignition_localhost = []
#Instanciamos el objeto de la clase creada para el webdriver
Ignition= WebDriverfunctions.WebDriverIgnition()
#Inicializamos el webdriver
Ignition.setup_method(Ignition_localhost)
#Relizamos el reseteo de la trial
Ignition.reset_trial(sUrlIgniton,sUser,sPassword)
#Cerramos el webdriver
Ignition.teardown_method(Ignition_localhost)
