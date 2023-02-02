from bertopic import BERTopic
from connect_mongodb import read_from_db
from nlp_preprocessing import nlp_pipeline
import pickle 


def apply_bertopic(data):
    topic_model = BERTopic(language = 'multilingual', n_gram_range = (1,2))
    topics, probs = topic_model.fit_transform(data)
    topic_model.get_topic_info()
    topic_model.visualize_topics()
    pickle.dump(topic_model, open('bertopic_musk.pkl', 'wb'))


if __name__ == "__main__":
    raw_text = read_from_db('tweets_wsc', 'tweets_m')
    date, usernames, tweets = nlp_pipeline(raw_text)
    apply_bertopic(tweets)