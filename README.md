# NER-with-Tensorflow
The repo contains the code to build a named entity recognition system that can identify name, address and organization names in text.

Articles from [Global News](https://globalnews.ca/) were crawled to test the model. The NER model is based on [this example transformer model](https://keras.io/examples/nlp/ner_transformers/) and the model is trained on CoNLL 2003.

## Running the project

### Create an Anaconda virtual environment
```
conda create --name <env> --file requirements.txt
```

### Download helper script for CoNLL 2003
```
wget https://raw.githubusercontent.com/sighsmile/conlleval/master/conlleval.py
```

### Create Sqlite database and tables
```
python database.py
```

### Scrape Global News articles and store articles in table `article` and sentences in table `sentence`
```
python scrapper.py
```

### Train an NER model and store the recognized entities in table `ner`
Run Jupyter Notebook `ner.ipynb`

## Testing
`test_db.py` contains two functions:

`get_articles_with_id()` prints out all articles with corresponding ids in the database.  
`get_ners(article_id)` prints out recognized entities from the article with the corresponding `article_id`