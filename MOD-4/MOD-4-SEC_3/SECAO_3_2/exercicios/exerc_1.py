from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()


def scrape(url):
    chrome.get(url)

    quote = chrome.find_element(
        By.CLASS_NAME, 'text'
    ).get_attribute('innerHTML')

    print(quote)


scrape('https://quotes.toscrape.com/')
