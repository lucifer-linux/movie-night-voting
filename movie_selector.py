import random
import os
from google_sheets_pull import *

def movie_list(responses):
    unwatched_list = []
    for record in responses.get_all_records():
        #specific filter for movie list data
        if record['Watched?'] == 'N':
            unwatched_list.append(record['What is the name of the Movie'])
    return unwatched_list

def random_list(list, n):
    selections = []
    while len(selections) < n:
        choice = random.choice(list)
        if choice not in selections:
            selections.append(choice)
    return selections

#string for discord poll
print(f'!poll [Please select a movie for tonight] {", ".join(random_list(movie_list(responses),3))}')