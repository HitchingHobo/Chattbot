import csv
import datetime
import random
import re

file = open('movies.csv', encoding='utf8')
dictlist = csv.DictReader(file)


def does_film_exists(value):
    for row in dictlist:
        if row['original_title'] == value:
            print("Det funkar!")
            file.seek(0)
            return True
    file.seek(0)
    return film_not_existing()

def film_not_existing():
    film_not_existing_list= [
                'Film does not exist, please try again',
                'I like The Shawshank Redemption, maybee try that?',
                'Did you spell that correctly? ',
                'Are you sure that was the right title?',
            ]
    return print(random.choice(film_not_existing_list))

def did_you_mean():
    if identified_film == False:
        print("I didn't find any movies named", current_film,) 
        for i in tiplist:
            print("Type 'yes' if you ment", i)
            q_answer = input()
            if q_answer == 'yes':
                current_film = i
                search_in_dict()
            elif q_answer != 'yes':
                continue

def choose_info(value):
    print('What would you like to learn?')
    print('I can tell you about the year, the actors, duration, give you a description and more')
    print('Seperate your input by commas')
    incoming_info = input()
    incoming_info.lower()
    ## Kanske fixa split-listen bättre
    ## Kanske ändra 'or' till listfunktion med 'any'
    iil = re.split(',| ', incoming_info)
    
    if 'year'in iil or 'released' in iil or 'premier' in iil or 'released' in iil:
        print('Released', get_year(value))
        
    if 'genre' in iil or 'genres' in iil or 'type' in iil or 'class' in iil or 'style' in iil or 'category' in iil:
        print(get_genre(value))
        
    if 'duration' in iil or 'runtime' in iil or 'length' in iil or 'time' in iil:
        print('Runtime of', get_duration(value))
        
    if 'director' in iil or 'directed' in iil or 'by' in iil or 'directors' in iil:
        print('Directed by', get_director(value))
        
    if 'writer' in iil or 'writers' in iil or 'author' in iil or 'scriptwriter' in iil in iil:
        print(get_writer(value))
        
    if 'production' in iil or 'producer' in iil or 'company' in iil or 'maker' in iil or 'produced by' in iil:
        print(get_production_company(value))
        
    if 'actors' in iil or 'actor' in iil or 'starring' in iil or 'cast'in iil or 'castmembers' in iil or 'roles' in iil or 'star' in iil:
        print(get_actors(value))
        
    if 'description' in iil or 'information' in iil or 'info' in iil or 'describe' in iil or 'summary' in iil or 'story' in iil:
        print(get_description(value))
        
    if  'vote' in iil or 'score' in iil or 'votes' in iil or 'total' in iil or 'points' in iil or 'count' in iil or 'record' in iil or 'result' in iil or 'rating' in iil or 'ratings' in iil:
        print('Averege vote of', get_avg_vote(value))
        print('Total votecount of', get_votes(value))


##Getters
def get_year(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            return row['year']
            
def get_genre(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            return row['genre']
        
def get_duration(value):
    for row in dictlist:
        if value == row['original_title']:
            duration_format = str(datetime.timedelta(minutes=int(row['duration'])))
            file.seek(0)
            return duration_format
        
def get_director(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            return row['director']
        
def get_writer(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            return row['writer']
        
def get_production_company(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            return row['production_company']
        
def get_actors(value):
    actor_list_final = []
    for row in dictlist:
        if value == row['original_title']:
            actor_str = row['actors']
            actor_list = actor_str.split(',')
            for i in range (5):
                actor_list_final.append(actor_list[i])
            file.seek(0)
            return actor_list_final
          
def get_description(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            return row['description']     
        
def get_avg_vote(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            return row['avg_vote']    

## fixa strängformattering på siffrorna     
def get_votes(value):
    for row in dictlist:
        if value == row['original_title']:
            file.seek(0)
            votes = row['votes']
            return votes