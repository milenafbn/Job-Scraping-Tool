import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

nltk.download('stopwords')

root = tk.Tk()
root.withdraw()  # Oculta a janela principal
url = simpledialog.askstring("Entrada", "Digite o link da página de pesquisa de vagas:")

driver = webdriver.Chrome()
print("driver iniciado")

#função de navegação e extração das descrições das vagas
def get_jobs(link):
    driver.get(link)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    jobs_descriptions = []

    link_vagas = soup.find_all('a', class_='sc-4d881605-1 IKqnq')

    for link in link_vagas:
        vaga_url = link.get('href')
        driver.get(vaga_url)
        time.sleep(5)

        soup_vaga = BeautifulSoup(driver.page_source, 'html.parser')

        requisitos_section = soup_vaga.find('h2', string="Requisitos e qualificações")
        
        if requisitos_section:
            # div_tags = soup_vaga.find_all('div', class_='sc-add46fb1-3')
            div_requisitos = requisitos_section.find_next_sibling('div')

            if div_requisitos:
                # tag_requisitos = div_tags[2]
                print("div_requisitos: ", div_requisitos)
                jobs_descriptions.append(div_requisitos.text)
            else:
                print("Nenhuma lista de requisitos encontrada")
        else:
            print("Título 'Requisitos e qualificações' não encontrado")

    return jobs_descriptions

def gerar_nuvem_palavras(descricoes):
    texto_total = ' '.join(descricoes)

    stop_words = set(stopwords.words('portuguese'))
    palavras = word_tokenize(texto_total)
    palavras_filtradas = [word for word in palavras if word.lower() not in stop_words and word.isalpha()]

    texto_filtrado = ' '.join(palavras_filtradas)

    wordcloud = WordCloud(width=800, height=400, max_font_size=150, background_color='white').generate(texto_filtrado)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    if url:
        descricoes = get_jobs(url)

        if descricoes:
            gerar_nuvem_palavras(descricoes)
        else:
            print('Nenhuma descrição encontrada')
        driver.quit()
    else:
        print('Nenhum link informado')

#  cd C:\Users\Milena\Downl.\venv\Scripts\Activate
#  python main.pyeu 