from connect_mongodb import read_from_db
import string 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from langdetect import detect
import re

'''
Main script for natural language processing preprocessing - language detection, text cleaning'''

def detect_language_tweet(tweet):
    language = 'english'
    languages = ['hungarian',
                'swedish',
                'kazakh',
                'norwegian',
                'finnish',
                'arabic',
                'indonesian',
                'portuguese',
                'turkish',
                'azerbaijani',
                'slovene',
                'spanish',
                'danish',
                'nepali',
                'romanian',
                'greek',
                'dutch',
                'README',
                'tajik',
                'german',
                'english',
                'russian',
                'french',
                'italian']
    try:
        language = detect(tweet)
        language = [lang for lang in languages if language in lang[:2]]
        if language == []:
            language = 'english'
    except : pass
    return language

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030" "]+", re.UNICODE)
    return re.sub(emoj, ' ', data)

def preprocessing_text(sentence, stopwords_extra_list = ['elon', 'musk', 'twitter']):
    clean_sentence = sentence.lower()
    clean_sentence = ' '.join(clean_sentence.splitlines())
    clean_sentence = re.sub(r'http\S+', '', clean_sentence)
    clean_sentence = re.sub(r'@\S+', '', clean_sentence)
    clean_sentence = remove_emojis(clean_sentence)
    clean_sentence = clean_sentence.translate(str.maketrans(' ', ' ', string.punctuation))
    clean_sentence   = clean_sentence.translate(str.maketrans("", "", "0123456789"))
    language = detect_language_tweet(clean_sentence)
    stop_words = stopwords.words(language)
    stop_words.extend(stopwords_extra_list)
    tokens = word_tokenize(clean_sentence)
    clean_sentence_list = ' '.join([word for word in tokens if word not in stop_words and len(word) > 2 and word != '  ' ])
    return clean_sentence_list

def nlp_processing(raw_text):
    date = [raw_text_ind['date'] for raw_text_ind in raw_text]
    usernames = [raw_text_ind['username'] for raw_text_ind in raw_text]
    tweets = [raw_text_ind['content'] for raw_text_ind in raw_text]
    clean_tweets = [preprocessing_text(tweet) for tweet in tweets if len(tweet) > 1 ]
    return date, usernames, clean_tweets



