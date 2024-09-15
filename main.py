import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from wordcloud import WordCloud
import matplotlib.pyplot as plt

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')


nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')


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
                # print("div_requisitos: ", div_requisitos)
                jobs_descriptions.append(div_requisitos.text)
            else:
                print("Nenhuma lista de requisitos encontrada")
        else:
            print("Título 'Requisitos e qualificações' não encontrado")

    return jobs_descriptions

def filtrar_texto(texto):
    texto_total = ' '.join(texto)

    stop_words = set(stopwords.words('portuguese'))
    stop_words.update(['informação','consumo','linguagens','documentação','crítica','utilização','anos','serviço','facilidade','utilizadas','lógica','cursos','monitoramento','preferencilamente','equipes','review','escalável','área','análise','análise','intermediário','técnicos','requisitos','integração','ensino','mercado','completo','experiência', 'conhecimento', 'habilidades', 'desenvolvimento', 'soluções', 'projetos', 'trabalho', 'fazer', 'criar', 'bom', 'excelente', 'e', 'ou', 'em', 'um', 'as', 'necessárias', 'necessários', 'necessária', 'necessário', 'desejável', 'desejáveis', 'desejada', 'desejado', 'diferencial', 'diferenciais', 'ser', 'ter', 'conhecimentos', 'básicos','básico', 'avançados', 'avançadas', 'básicas', 'uso', 'obter', 'aplicação','time', 'tecnologia','outros', 'qualificações', 'framework', 'ferramentas', 'trabalha', 'programação', 'testes', 'continua'])

    tokens = word_tokenize(texto_total)
    tagged = pos_tag(tokens)
    palavras_filtradas = [word for word, tag in tagged if tag.startswith('N') and word.lower() not in stop_words and word.isalpha()]
    texto_filtrado = ' '.join(palavras_filtradas)

    return texto_filtrado

def gerar_nuvem_palavras(descricoes):

    wordcloud = WordCloud(width=800, height=400, max_font_size=150, background_color='white').generate(descricoes)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    if url:
        descricoes = get_jobs(url)

        if descricoes:
            texto_filtrado = filtrar_texto(descricoes)
            if texto_filtrado:
                gerar_nuvem_palavras(texto_filtrado)
            else:
                print('Nenhum texto filtrado')
        else:
            print('Nenhuma descrição encontrada')
        driver.quit()
    else:
        print('Nenhum link informado')

#  cd C:\Users\Milena\Downl.\venv\Scripts\Activate
#  python main.pyeu 