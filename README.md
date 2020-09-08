# movie-night-voting
The intention of this code is to make it easy to select a movie from a list of movies.


### google_sheets_pull.py
    cred_path
This is a api token which is not pushed to github from my repository. A token can be requested from https://console.cloud.google.com/

    movie_sheet
This is specific to my use. A google form is pushing responses to the google sheet called "Movie Night Form (Responses)" 
### movie_selector.py
    specific sheet columns
  In the sheet of my use case, the columns "What is the name of the Movie" and "Watched" are called to for the un_watched list for a random selection to vote on in my discord server. 
