import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

def login_twitter_scrap_tweets(username = '', password = '', email = '', query = '', tweets = 0):
    driver = Firefox()
    driver.get('https://twitter.com/login')
    xpath_username = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
    time.sleep(5)
    username = driver.find_element(By.XPATH, xpath_username).send_keys(username)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
    time.sleep(5)
    password_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    driver.find_element(By.XPATH, password_xpath).send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
    time.sleep(3)
    try:
        if driver.find_element(By.XPATH, '//input[@inputmode="email"]'):
            driver.find_element(By.XPATH, '//input[@inputmode="email"]').send_keys(email)
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span').click()
    except:pass
    time.sleep(3)
    try:
        if driver.find_element(By.CSS_SELECTOR, '.r-16l9doz > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > img:nth-child(2)'):
            driver.find_element(By.CSS_SELECTOR, 'div.r-s8bhmr:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1)').send_keys(Keys.ENTER)
    except: pass
    driver.find_element(By.XPATH, '//input[@aria-label="Search query"]').send_keys(query).send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/div/span').send_keys(Keys.ENTER)
    tweets_list = [driver.find_element(By.XPATH, '//div[@testid="tweetText"]')  for _ in range(tweets)]
    time.sleep(3)
    driver.close()
    return tweets_list

if __name__ == '__main__':
    username = input("Twitter username : ")
    password = input("Twitter password: ")
    email = input("Twitter email: ")
    query = input("Twitter search query: ")
    no_tweets = input("Number of tweets required: ")
    login_twitter_scrap_tweets(username = str(username), password = str(password), email = str(email), query = str(query), tweets = int(no_tweets))
