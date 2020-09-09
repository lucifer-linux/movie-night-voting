import random
import os
from utilities import *

def find_unwatched(responses):
    unwatched = []
    for record in responses.get_all_records():
        #specific filter for movie list data
        if record['Watched?'] == 'N':
            unwatched.append(record['What is the name of the Movie'])
    return unwatched

def random_list(selections_available, n):
    selections = []
    while len(selections) < n:
        choice = random.choice(selections_available)
        if choice not in selections:
            selections.append(choice)
    return selections

cred_path = '../keys/drive_api.json'
sheet_name = 'Movie Night Form (Responses)'

responses = pull_responses(cred_path,sheet_name)

#string for discord poll
movies = random_list(find_unwatched(responses),3)
print(f'!poll [Please select a movie for tonight] {", ".join(movies)}\n')
for movie in movies:
    print(f'{movie}: {find_imdb(movie)}')