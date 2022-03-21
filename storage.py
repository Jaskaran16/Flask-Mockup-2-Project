import csv 
all_movies =  []
with open("Flask Mockup 2.csv") as fm:
    reader = csv.reader(fm)
    data = list(reader)
    all_movies = data[1:]
liked_movies = []
not_liked_movies = []
did_not_watch = []
