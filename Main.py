from Funktioner import *

history_list = []

while True: 
    movie_title = input("Vilken film har du funderingar kring? ")
    movie_title = movie_title.lower()
    movie_title = movie_title.title()
    if does_film_exists(movie_title) is True:
        choose_info(movie_title)


# print(does_film_exists(film))          
# print()
# print (film)
# print(get_year(film))
# print(get_genre(film))
# print(get_duration(film))
# print(get_director(film))
# print(get_writer(film))
# print(get_producation_company(film))
# print(get_actors(film))
# print(get_description(film))
# print(get_avg_vote(film))
# print(get_votes_nr(film))
