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

print(f"\nOrijinal Söz: {quote}\n\nÇeviri: {quote_tr}\n\nYapım: {show}\n\n")

# ACRZeuss
ia = imdb.IMDb()
# ACRZeuss
show_search = ia.search_movie(show)[0]
fullsize_cover = show_search["full-size cover url"]
# ACRZeuss
no = ["evet", "e"]
download_poster = input(f"{show} filminin/dizisinin posterini indirmek ister misin? (evet/hayır): ")
# ACRZeuss
if download_poster.lower() in no: 
    print("Poster indirilmedi.")
    exit()
else:
    wget.download(fullsize_cover, show + ".jpg")
    print("Poster indirildi. İndirilmediyse destek için https://github.com/ACRZeuss/film-veya-diziden-replik-cekme/issues adresinde bir issue (hata geribilidirimi) açabilirsiniz.")
    
# ACRZeuss
