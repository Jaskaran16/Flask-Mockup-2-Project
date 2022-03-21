import csv
with open("Movie Data.csv", encoding="utf-8") as m:
    reader = csv.reader(m)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
headers.append("poster_link")
with open("Flask Mockup 2.csv", "a+", encoding="utf-8") as fm:
    csvwriter = csv.writer(fm)
    csvwriter.writerow(headers)
with open("Movie Links.csv", encoding="utf-8") as ml:
    reader = csv.reader(ml)
    data = list(reader)
    all_movie_links = data[1:]
for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_links_items for movie_links_items in all_movie_links)
    if poster_found:
        for movie_links_items in all_movie_links:
            if movie_item[8] == movie_links_items[0]:
                movie_item.append(movie_links_items[1])
                if len(movie_item) == 28:
                    with open("Flask Mockup 1.csv", "a+", encoding="utf-8") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)