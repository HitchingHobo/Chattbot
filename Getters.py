
import csv
import datetime



file = open('movies.csv', encoding='utf8')
dictlist = csv.DictReader(file)


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