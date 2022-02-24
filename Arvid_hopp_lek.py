import csv
import random

filmen='The Shawshank Redemption'
file = open('movies.csv', encoding='utf-8')
dictlist = csv.DictReader(file)

def say_hello():
    print("Welcome to Moviebot!")

def choices():
    print("What do you want to know about: ", movie_title, " ? " )


def does_film_exists(value):
    for row in dictlist:
        if row['original_title'] == value:
            print("Det funkar!")
            return True
        else:
            film_not_existing()
            return False

def film_not_existing():
    film_not_existing_list= [
                'Film does not exist, please try again',
                'I like The Shawshank Redemption, maybee try that?',
                'Are you stupid? That movie is not on the top 100 list... ',
                'Are you sure that was the right title?',
            ]
    return print(random.choice(film_not_existing_list))

while True: 
    say_hello()
    movie_title = input("Vilken film har du funderingar kring? ")
    if does_film_exists(movie_title) is True:
        choices()
