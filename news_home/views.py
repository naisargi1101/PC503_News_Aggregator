from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)


# GEtting news from Inshorts

inshorts_r = requests.get("https://inshorts.com/en/read/")
inshorts_soup = BeautifulSoup(inshorts_r.content, 'html.parser')

inshorts_headings = inshorts_soup.find_all('span', attrs={'itemprop': 'headline'})
# toi_head = toi_soup.find_all('span', attrs={'itemprop': 'headline'})

inshorts_headings = inshorts_headings[0:] # removing footers

# toi_head = toi_head[0:-13]
inshorts_news = []

for th in inshorts_headings:
    inshorts_news.append(th.text)

inshorts_headlines = []

#Getting news from Hindustan times

# ht_r = requests.get("https://www.hindustantimes.com/india-news/")
# ht_soup = BeautifulSoup(ht_r.content,  features="xml")
# ht_headings = ht_soup.findAll("h3", attrs={"class": "hdg3"})
# print(ht_headings)
# ht_headings = ht_headings[2:]
# ht_news = []

# for hth in ht_headings:
#     ht_news.append(hth.text)
# #print(ht_news)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'inshorts_news': inshorts_news})