from bs4 import BeautifulSoup
import requests
import re
from decimal import Decimal, ROUND_DOWN


# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)                 # HTTP request to the specified URL and save the response from server in a response object
# Created a BeautifulSoup object by passing two arguments:
soup = BeautifulSoup(response.text, 'lxml')  # response object's content will be in the form of text.   lxml = HTML parser we want to use.

# Visual representation of the parse tree created from the raw HTML content.
# print(soup.prettify())

movies = soup.select('td.titleColumn')       # td is table data html tag.  Movies is list
# print('\n', movies, '\n')

crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]   # Tapping into <a/> tag attributes in the anchor tag present inside td html tag having titleColumn class.
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, 50):
    # Separate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()   # Tap into every element present inside the movies, and convert them to string
    # print(movie_string)

    movie = (' '.join(movie_string.split()).replace('.', ''))  # Split the string and join it with space btw every part of the splitted string ,then you replace . with ' '
    # print(movie)

    movie_title = movie[len(str(index)) + 1:-7]    # ex : 50 Rear Window (1954)
                                                    # len(index) =2 + one space : reverse indexing -7 characters.

    place = movie[:len(str(index)) - (len(movie))]  # ex :  50 Rear Window (1954)
                                                    # start from 0th index, Do reverse indexing index length - length of whole movie string

    data = {"movie_title": movie_title,
            "place": place,
            "star_cast": crew[index],
            "rating": Decimal(ratings[index]).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            }
    imdb.append(data)

# Printing the data :
for item in imdb:
    print(item['place'], '-', item['movie_title'], ',', 'Actors:', item['star_cast'], ', Rating :', item['rating'])
