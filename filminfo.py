import csv

filmen='The Shawshank Redemption'
file = open('movies.csv', encoding='utf8')

dictlist = csv.DictReader(file)

for row in dictlist:
    if row['original_title'] == filmen:
        print(row['year'])
        print('FUCK YES')
    #print(row['year'], row['original_title'])
    #print('')

