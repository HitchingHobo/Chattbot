import csv
import random
import re
from TextReader import *
from Getters import *


 
def does_film_exists(value):
    for row in dictlist:
        if row['original_title'] == value:
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

#def did_you_mean():
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
    
    if list_check(iil, year_list) == True:
        print('Released', get_year(value))
        
    if list_check(iil, genre_list) == True:
        print(get_genre(value))
        
    if list_check(iil, duration_list) == True:
        print('Runtime of', get_duration(value))
        
    if list_check(iil, director_list) == True:
        print('Directed by', get_director(value))
        
    if list_check(iil, writer_list) == True:
        print(get_writer(value))
        
    if list_check(iil, producer_list) == True:
        print(get_production_company(value))
        
    if list_check(iil, actors_list) == True:
        print(get_actors(value))
        
    if list_check(iil, description_list) == True:
        print(get_description(value))
        
    if  list_check(iil, vote_list) == True:
        print('Averege vote of', get_avg_vote(value))
        print('Total votecount of', get_votes(value))

def list_check(list1, list2):
    check = any (item in list1 for item in list2)
    return check
