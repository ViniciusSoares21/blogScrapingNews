from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def scrape_links_news(browser):
    browser.get("https://blog.betrybe.com/")
    links_news = []
    for link in browser.find_elements(By.CLASS_NAME, "cs-overlay-link"):
        links_news.append(link.get_attribute("href"))

    return links_news


def create_object_news(link_page, browser):
    browser.get(link_page)
    sleep(2)
    news = {}
    news["title"] = browser.find_element(By.CLASS_NAME, "entry-title").text
    news["image"] = browser.find_element(
        By.CSS_SELECTOR, "div.entry-overlay.cs-overlay-background img"
    ).get_attribute("src")
    try:
        timestamp_element = browser.find_element(By.CLASS_NAME, "meta-date")
    except NoSuchElementException:
        timestamp_element = browser.find_element(
            By.CLASS_NAME, "post-modified-info"
        )

    news["timestamp"] = timestamp_element.text
    news["titleContents"] = browser.find_element(By.ID, "1").text
    contents = []
    for tag_p in browser.find_element(By.ID, "1").find_elements(
        By.XPATH, "./following-sibling::p[position() <= 3]"
    ):
        contents.append(tag_p.text)
    news["contents"] = contents
    news["category"] = browser.find_element(By.CLASS_NAME, "label").text
    return news


def scrape_news():
    browser = webdriver.Firefox()
    links = scrape_links_news(browser)
    news = []
    for link_page in links:
        news.append(create_object_news(link_page, browser))
    browser.quit()
    return news
