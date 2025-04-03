from selenium import webdriver
from selenium.webdriver.common.by import By
import wget
import os

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
navegador = webdriver.Chrome()

navegador.get(URL)

# passa pelo botão de cookies do site
btn_cookies = navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]')
btn_cookies.click()


# baixa o primeiro PDF
primeiro_pdf = navegador.find_element(By.XPATH, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]')
primeiro_pdf.click()

navegador.switch_to.window(navegador.window_handles[-1])

url_pagina1 = navegador.current_url

pasta_destino = "C:Users/Fabri/Downloads/"

download_1 = wget.download(url_pagina1, "anexo_1_rol.pdf")

# baixa o segundo pdf


input("Pressione Enter para fechar... ")
navegador.quit()
