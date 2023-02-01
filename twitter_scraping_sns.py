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
    query = 'musk'
    no_tweets = 10000
    tweets = twitter_scraping_sns(query, no_tweets)
    for tweet in tweets:
        connect_mongodb.insert_data_mongodb(document_to_insert=tweet)
    print('Done')