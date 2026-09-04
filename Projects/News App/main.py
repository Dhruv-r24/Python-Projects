import requests
from errors import *
import os

while True:
    try:
        query = input('Enter the title of the article you want to discover: ').lower().replace(' ', '')
        n_of_articles = int(input('How many number of articles you want to see: '))

        if n_of_articles < 0:
            raise NegativeIntegerError

        elif n_of_articles == 0:
            print('Number of articles cannot be 0')
            continue

        break

    except ValueError:
        print('Invalid Value')
    except NegativeIntegerError:
        print('Negative integers not allowed!')


API_KEY = os.getenv('NEWSAPI_KEY', '1dce58237c35413caa8450cd1f1af319')  # fallback for now, move to env var

url = f'https://newsapi.org/v2/everything?q={query}&from=2026-08-04&sortBy=publishedAt&apiKey={API_KEY}'

r = requests.get(url)
data = r.json()

if data.get('status') != 'ok':
    print(f"API error: {data.get('message', 'unknown error')}")
else:
    articles = data.get('articles', [])

    if not articles:
        print('No articles found for that query.')
    else:
        count = min(n_of_articles, len(articles))
        if n_of_articles > len(articles):
            print(f"Only {len(articles)} articles available; showing all of them.")

        for i, article in enumerate(articles[:count], start=1):
            title = article['title']
            link = article['url']
            print(f'Article {i} --> {title}\n Click here to access the whole article: {link}')
            print('\n ***********************************************************\n')
