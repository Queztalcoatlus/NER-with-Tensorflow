import sqlite3
DATABASE_NAME = 'global_news.db'


def main():
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS ner')
    cur.execute('DROP TABLE IF EXISTS sentence')
    cur.execute('DROP TABLE IF EXISTS article')
    cur.execute('''CREATE TABLE article (title TEXT UNIQUE)''')
    cur.execute('''CREATE TABLE sentence (sent TEXT, article_id INTEGER, FOREIGN KEY(article_id) REFERENCES article(rowid))''')
    cur.execute('''CREATE TABLE ner (entity TEXT, entity_type TEXT, sentence_id INTEGER, FOREIGN KEY(sentence_id) REFERENCES sentence(rowid))''')
    con.close()


if __name__ == "__main__":
    main()