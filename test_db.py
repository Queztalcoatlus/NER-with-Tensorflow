import sqlite3
from database import DATABASE_NAME


def get_articles_with_id():
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute('''
    SELECT rowid, title FROM article
    ''')
    rows = cur.fetchall()
    for id, title in rows:
        print(f'id: {id}, title: {title}')
    con.close()

def get_ners(article_id):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute('''
    SELECT entity, entity_type, sentence_id, sent, title 
    FROM article a
    INNER JOIN sentence s ON a.rowid = s.article_id
    INNER JOIN ner n ON n.sentence_id = s.rowid
    WHERE a.rowid = ?''', (article_id,))
    rows = cur.fetchall()
    for entity, entity_type, sentence_id, sent, title in rows:
        print(f'entity: {entity}, entity_type: {entity_type}, sent_id: {sentence_id}, sent: {sent}, title: {title}\n')