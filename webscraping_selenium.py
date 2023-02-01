from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    browser = Firefox()
    browser.get('https://twitter.com/login')
    username = browser.find_element(By.XPATH,'//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
    username.send_keys('popovici.cristina1221@gmail.com')
    username.send_keys(Keys.RETURN)