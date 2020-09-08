import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

#location for credential file from google drive api. Renamed to "drive_api.json"
cred_path = '../keys/drive_api.json'
cred = ServiceAccountCredentials.from_json_keyfile_name(cred_path,scope)
client = gspread.authorize(cred)

#name of form where data is located
movie_sheet = "Movie Night Form (Responses)"
responses = client.open(movie_sheet).sheet1