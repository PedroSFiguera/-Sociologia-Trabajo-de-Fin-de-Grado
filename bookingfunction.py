import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

# ESTO YA FUNCIONA, AHORA, QUIZÁS PUEDA METER TODO LO DEL ANÁLISIS EN UNA FUNCIÓN Y HACER UNA LISTA CON LAS URLS
# Y QUE LAS VAYA ANALIZANDO UNA A UNA PARA NO TENER QUE HACER UN SCRIPT PARA CADA PAGINA QUE QUIERO ANALIZAR. LO PROBARÉ
# EN OTRO ARCHIVO

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 "
    "Chrome/71.0.3578.80 Safari/537.36")

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s, options=opts)


# EL PROBLEMA ES QUE LOS NIVELES DE SEGURIDAD SON MUY ESTRICTOS EN CUANTO VEN QUE SOY UN BOT O ALGO ASÍ.
# LO QUE HARE ES IR PAGINA POR PAGINA PUES CON SELENIUM PARA SALTARME ESTO.

columns = ['Nombre', 'Informacion', 'Instructores', 'ActividadesOpcionales', 'Alimentacion']
data = []

urls = ['https://www.bookyogaretreats.com/es/be-mindfulyoga/7-dias-de-meditacion-asanas-y-profunda-filosofia-del-yoga-junto-a-la-playa-en-cullera-valencia',
        'https://www.bookyogaretreats.com/es/be-mindfulyoga/5-dias-de-meditacion-asanas-y-filosofia-de-yoga-profundo-junto-a-la-playa-en-cullera-valencia',
        'https://www.bookyogaretreats.com/es/matrika-yoga-y-desarrollo-personal/4-dias-de-retiro-de-yoga-iyengar-hatha-yoga-y-meditacion-en-avila-gredos',
        'https://www.bookyogaretreats.com/es/escuela-evolutiva/3-dias-de-retiro-de-meditacion-el-poder-del-silencio-en-barcelona',
        'https://www.bookyogaretreats.com/es/murtra-galilea/3-dias-de-retiro-de-bienestar-emocional-y-yoga-en-chiclana-de-la-frontera-cadiz',
        'https://www.bookyogaretreats.com/es/centro-yoga-y-arte/3-dias-de-retiro-de-yoga-aereo-baile-de-fuego-y-magia-en-motril-costa-tropical',
        'https://www.bookyogaretreats.com/es/can-mussol-anima-mundi-retreat-center/3-dias-de-retiro-rural-de-yoga-en-fonollosa-cataluna',
        'https://www.bookyogaretreats.com/es/centro-de-nutricion-y-bienestar-casa-la-joya/10-dias-de-retiro-de-yoga-ayuno-y-meditacion-en-playa-de-la-joya-costa-tropical']

def scraping():
    driver.get(
        'https://www.bookyogaretreats.com/es/be-mindfulyoga/7-dias-de-meditacion-asanas-y-profunda-filosofia-del-yoga'
        '-junto-a-la-playa-en-cullera-valencia')

    sleep(random.randint(5, 10))
    name = driver.find_element(By.XPATH, '//h1[@class="listing-title__title title listing-title-new"]').text
    info_general = driver.find_element(By.XPATH, '//div[@class="listing-overview__introduction"]//p').text
    instructores = driver.find_element(By.XPATH, '//div[@class="listing-description-container"]/ul').text
    sleep(random.randint(5, 10))
    actividades_opcionales = driver.find_element(By.XPATH, '//div[@data-attr="lp-itinerary"]').text
    alimentación = driver.find_element(By.XPATH, '//div[@data-attr="lp-food"]').text
    sleep(random.randint(2, 5))
    data.append([name, info_general, instructores, actividades_opcionales, alimentación])


df = pd.DataFrame(data, columns=columns)
df.to_csv('pagina1.csv')
