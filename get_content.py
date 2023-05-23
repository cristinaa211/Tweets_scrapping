import requests
from bs4 import BeautifulSoup as bs 


def web_scraping(list_of_urls, headers):
    for url_link in list_of_urls:
        response = requests.get(url_link, headers= headers)
        html_content = bs(response.content, 'html.parser')
        html_content.prettify()
        things = html_content.get_text()
        things = html_content.find_all('p')
        print(things)
    return things


if __name__ == '__main__':
    headers={'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    url_user = input("Please specify an url that allows web scraping: ")
    search_query = input("Please provide with a search query:")
    url = [url_user]
    things = web_scraping(url, headers=headers)

