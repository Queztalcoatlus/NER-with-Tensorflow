import requests
from bs4 import BeautifulSoup
import re, random
from time import sleep
import sqlite3
from database import DATABASE_NAME

def scrap(url):
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        return False
    soup = BeautifulSoup(response.content, 'html5lib')
    link_set = set()
    for a in soup.find_all('a', href=re.compile('https://globalnews.ca/news/\d+/')):
        link = a['href']
        if link not in link_set:
            try:
                sleep(random.randint(1, 3))
                parse_article_link(link)
                link_set.add(link)
            except Exception as e:
                print(e)
                continue
    return True


def parse_article_link(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html5lib')
    title = soup.find('h1', {'class': 'l-article__title'})
    print(title.text)
    article = soup.find('article')
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute('''
    INSERT INTO article (title)
    VALUES(?);
    ''', (title.text, ))
    article_id = cur.lastrowid
    for p in article.find_all('p'):
        cur.execute('''
        INSERT INTO sentence (sent, article_id)
        VALUES(?, ?);
        ''', (p.text, article_id))
    con.commit()
    con.close()


if __name__ == "__main__":
    url = 'https://globalnews.ca/'
    scrap(url)