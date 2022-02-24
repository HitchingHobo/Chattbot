import csv
import datetime

file = open('movies.csv', encoding='utf8')
dictlist = csv.DictReader(file)

film = 'The Godfather'

def get_year():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['year']
            
def get_genre():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['genre']
        
def get_duration():
    global film
    for row in dictlist:
        if film == row['original_title']:
            duration_format = str(datetime.timedelta(minutes=int(row['duration'])))
            file.seek(0)
            return duration_format
        
def get_director():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['director']
        
def get_writer():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['writer']
        
def get_producation_company():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['production_company']
        
def get_actors():
    global film
    actor_list_final = []
    for row in dictlist:
        if film == row['original_title']:
            actor_str = row['actors']
            actor_list = actor_str.split(',')
            for i in range (5):
                actor_list_final.append(actor_list[i])
            file.seek(0)
            return actor_list_final
          
def get_description():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['description']     
        
def get_avg_vote():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['avg_vote']    
        
def get_votes_nr():
    global film
    for row in dictlist:
        if film == row['original_title']:
            file.seek(0)
            return row['votes']     
          
                
print(film)
print(get_year())
print(get_genre())
print(get_duration())
print(get_director())
print(get_writer())
print(get_producation_company())
print(get_actors())
print(get_description())
print(get_avg_vote())
print(get_votes_nr())