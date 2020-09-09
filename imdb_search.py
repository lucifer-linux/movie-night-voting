import requests
from bs4 import BeautifulSoup


imdb_search = 'https://www.imdb.com/find?'
imdb_home = 'https://www.imdb.com'

def find_imdb(movie_name):
    query = {'q':movie_name}
    search = requests.post(imdb_search, data=query)
    soup = BeautifulSoup(search.text, features="html.parser")
    results = soup.find_all('td',class_='result_text')
    if len(results) != 0:
        relative_link = soup.find_all('td',class_='result_text')[0].a['href']
        link = imdb_home + relative_link
    else: 
        link = f'[ERROR] {movie_name} not found on IMDB, check the name'
    return link
