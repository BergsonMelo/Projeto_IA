import requests
from bs4 import BeautifulSoup

def get_news_from_g1():
    # URL do site G1
    url = 'https://g1.globo.com/'

    try:
        # Realiza a requisição ao site com um User-Agent para simular um navegador
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        
        # Verifica se a requisição foi bem sucedida
        response.raise_for_status()

        # Parse do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontra notícias
        noticias = soup.find_all('div', class_='feed-post-body', limit=100)
        arr_noticias = []

        for noticia in noticias:
            # Extrai o título
            titulo = noticia.find('a', class_='feed-post-link')
            titulo_text = titulo.get_text(strip=True) if titulo else 'Título não encontrado'
            link = titulo['href'] if titulo else 'Link não encontrado'
            
            # Extrai a data de publicação
            data_publicacao = noticia.find('span', class_='feed-post-datetime')
            data_text = data_publicacao.get_text(strip=True) if data_publicacao else 'Data de publicação não encontrada'

            # Adiciona um dicionário com as informações da notícia na lista
            arr_noticias.append({
                'resumo': titulo_text,
                'link': link,
                'data_publicacao': data_text
            })

        return arr_noticias

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")