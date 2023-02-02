import snscrape.modules.twitter as snstw
import connect_mongodb


def twitter_scraping_sns(query, no_tweets):
    tweets = []
    for tweet in snstw.TwitterSearchScraper(query=query).get_items():
        if len(tweets) != no_tweets:
            tweets.append({'date' : tweet.date, 'username': tweet.user.username, 'content' : tweet.rawContent})
        else : break
    return tweets

if __name__ == '__main__':
    query = 'biden'
    no_tweets = 10000
    tweets_biden = twitter_scraping_sns(query, no_tweets)
    print('I am scraping tweets of trump now.')
    tweets_trump = twitter_scraping_sns('trump', no_tweets)
    connect_mongodb.insert_data_mongodb( collection_name='joe_biden',document_to_insert=tweets_biden)
    connect_mongodb.insert_data_mongodb( collection_name='donald_trump',document_to_insert=tweets_trump)
    print('Done')