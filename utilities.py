import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def pull_responses(cred_path,sheet_name):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive'
        ]

    #location for credential file from google drive api. Renamed to "drive_api.json"
    cred = ServiceAccountCredentials.from_json_keyfile_name(cred_path,scope)
    client = gspread.authorize(cred)

    #name of form where data is located
    responses = client.open(sheet_name).sheet1
    return responses

def find_imdb(movie_name):
    imdb_search = 'https://www.imdb.com/find?'
    imdb_home = 'https://www.imdb.com'
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
