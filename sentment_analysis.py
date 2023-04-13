from sklearn.feature_extraction.text import TfidfVectorizer 
from bertopic import BERTopic
import connect_mongodb
from nlp_preprocessing import nlp_processing
import pickle 
from twitter_scraping_sns import extract_tweets
import os 
import pathlib 


def extract_tfidf_features(raw_text, vectorizer_name):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(raw_text)
    with open(vectorizer_name, 'wb') as f:
        pickle.dump(tfidf_vectorizer, f, protocol=pickle.HIGHEST_PROTOCOL)
    return tfidf_matrix

def apply_bertopic(data, dates, model_path, model_name):
    topic_model = BERTopic(language = 'multilingual', verbose = True )
    topics, probs = topic_model.fit_transform(data)
    print(topic_model.get_topic_info())
    topic_model.visualize_topics()
    representative_docs = topic_model.get_representative_docs()
    fig = topic_model.visualize_topics(top_n_topics = len(topics))
    fig.write_html("{}/{}_topics.html".format(model_path, model_name))
    hierarchical_topics =  topic_model.hierarchical_topics(data)
    fig = topic_model.visualize_hierarchical_documents(data, hierarchical_topics)
    fig.write_html("{}/{}_hierarchy.html".format(model_path, model_name))
    tree = topic_model.get_topic_tree(hierarchical_topics)
    with open('{}/tree.txt'.format(model_path), 'w',encoding='utf-8') as f:
        f.write(tree)
    topics_over_time = topic_model.topics_over_time(data, dates)
    fig = topic_model.visualize_topics_over_time(topics_over_time)
    fig.write_html("{}/{}_topics_over_time.html".format(model_path, model_name))
    fig = topic_model.visualize_barchart(top_n_topics = len(set(topics)))
    fig.write_html("{}/{}_barchart.html".format(model_path, model_name))
    with open('{}/{}.pkl'.format(model_path, model_name), 'wb') as f:
        pickle.dump(topic_model, f, protocol=pickle.HIGHEST_PROTOCOL)
    return topics, representative_docs

def text_analysis_pipeline(query, no_tweets, vectorizer_name, model_name):
    raw_tweets = extract_tweets(query, no_tweets)
    connect_mongodb.insert_data_mongodb( collection_name= 'tweets_{query}'.format(query) ,document_to_insert=raw_tweets)
    raw_text = connect_mongodb.read_from_db('tweets_wsc', 'tweets_{query}'.format(query))
    date, usernames, tweets = nlp_processing(raw_text)
    with open(vectorizer_name, 'rb') as f: vectorizer = pickle.load(f)
    with open(model_name, 'rb') as f : model = pickle.load(f)
    features = vectorizer.transform(tweets)
    predictions = model.transform(features)
    

if __name__ == "__main__":
    path = os.getcwd()
    vectorizer_name = pathlib.Path(path) / 'models/tfidf_vectorizer_tweets.pkl'
    model_path = pathlib.Path(path)
    model_name =  'models/bertopic_model.pkl'
    raw_text = connect_mongodb.read_from_db('tweets_wsc', 'tweets_m')
    date, usernames, tweets = nlp_processing(raw_text)
    # tfidf_matrix = extract_tfidf_features(tweets, vectorizer_name)
    topics, representative_docs = apply_bertopic(tweets, date, model_path, model_name)