import csv
with open('IMDB.CSV','r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    Rating = []
    for row in spreadsheet:
        movie_rank = row['Rating']
        Rating.append(movie_rank)

highest_rank = max(movie_rank)
print(highest_rank)
