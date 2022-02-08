# ACRZeuss
import requests
from googletrans import Translator
import imdb
import wget
# ACRZeuss
url = "https://movie-quote-api.herokuapp.com/v1/quote/"

response = requests.get(url)
data = response.json()
# ACRZeuss
translator = Translator()

quote = data['quote']
show = data['show']

quote_tr = translator.translate(quote, dest='tr').text
# ACRZeuss
print(" ")
print("Orjinal Söz: ", quote)
print(" ")
print("Çeviri: ", quote_tr)
print(" ")
print("Yapım: ", show)
print(" ")
# ACRZeuss
ia = imdb.IMDb()

show_name = show
# ACRZeuss
show_search = ia.search_movie(show_name)[0]

fullsize_cover = show_search["full-size cover url"]
# ACRZeuss
yes = "evet"
no = "hayır"

download_poster = input(show_name + " " + "filminin/dizisinin posterini indirmek ister misin? (Evet ya da Hayır): ")
# ACRZeuss
if download_poster.lower() == yes:
    wget.download(fullsize_cover, show_name + ".jpg")
if download_poster.lower() == no:
    exit()
# ACRZeuss
