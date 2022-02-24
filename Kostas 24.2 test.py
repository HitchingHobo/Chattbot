import csv

file = open('movies.csv', encoding='utf8')
dictlist = csv.DictReader(file)
identified_film = False

current_film = input('What movie would you like to know more about?\n')
current_film = current_film.lower()
current_film = current_film.title()

##Söker efter input titeln i vår lista, söker även efter delar av namnet och sparar i en "tipslista"
def search_in_dict():
    global identified_film, dictlist, tiplist, current_film
    tiplist = []
    for row in dictlist:
        current_film_split = current_film.split()
        if row['original_title'] == current_film:
            identified_film = True
            print('Ok', row['original_title'], 'came out', row['year'], 'and was directed by', row['director'])
        elif identified_film == False:
             for i in current_film_split:
                 if i in row['original_title']:
                     tiplist.append(row['original_title'])
    if identified_film == False:
        did_you_mean()
  
        
## tar reda på vilken info man vill söka upp      
def requested_info():
    global header
    req_info_list = []
    print('What would you like to know?')
    print("I can tell you about the film's year, director, cast, rating, description and more")
    while True:
        incoming_txt = input("Type in what category you'd like me to look up, type 'done' to finish\n")
        incoming_txt.lower()
        if incoming_txt in header:
            req_info_list.append(incoming_txt)
        elif incoming_txt == 'done':
            break
        else:
            print("I don't udnerstand your input, try again")
            continue
        if incoming_txt == 'done':
            break
    return req_info_list


## Printar ut fint när film och info är vald
def final_output(film, info):
    pass
          

##Läser upp "tipslistan" och frågar om tipset filmen stämmer med önskad sökning
def did_you_mean():
    global identified_film, current_film, tiplist
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


search_in_dict()


            
file.close()
