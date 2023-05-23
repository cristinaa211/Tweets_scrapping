import snscrape.modules.twitter as snstw
import connect_mongodb
import pandas as pd

def extract_tweets(query, no_tweets):
    tweets = []
    for tweet in snstw.TwitterSearchScraper(query=query).get_items():
        if len(tweets) != no_tweets:
            tweets.append({'date' : tweet.date, 'username': tweet.user.username, 'content' : tweet.rawContent})
        else : break
    return tweets

if __name__ == '__main__':
    query = str(input("Please specify a search query: "))
    no_tweets = int(input("Please specify the number of tweets you want to output."))
    tweets = extract_tweets(query, no_tweets)
    print('I am scraping tweets of {} now.'.format(query))
    try:
        connect_mongodb.insert_data_mongodb( collection_name= query, document_to_insert=tweets)
    except:
        dataframe = pd.DataFrame(tweets)
        csv_file = dataframe.to_csv("tweets_{}".format(query))
    print('Done')
