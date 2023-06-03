import time
import urllib.robotparser
from bs4 import BeautifulSoup
from selenium import webdriver


class WebURL:

    def __init__(self):
        self.url = input("Podaj adres URL lub wpisz 'EXIT' aby zakończyć działanie programu.\nURL>>> ")

    def get_url(self):
        return self.url


class Producer:

    def __init__(self, user_url):
        self.user_url = user_url

    def check_producer(self):
        if 'hopsteiner' in self.user_url:
            return 1
        elif 'hollingbery' in self.user_url:
            return 2
        elif 'crosbyhops' in self.user_url:
            return 3
        elif 'glacierhops' in self.user_url:
            return 4
        else:
            return 'Nie znaleziono producenta.'


class SoupSource:

    def __init__(self, user_url):
        self.user_url = user_url

    def get_source_code(self):
        driver = webdriver.Chrome()
        driver.get(self.user_url)
        time.sleep(1)
        html = driver.page_source
        source_soup = BeautifulSoup(html, 'html.parser')
        return source_soup


class CrawlChecker:

    producers_robotstxt = {1: 'https://www.hopsteiner.com/robots.txt',
                           2: 'https://www.hollingberyandson.com/robots.txt',
                           3: 'https://portal.crosbyhops.com/robots.txt',
                           4: 'https://glacierhopsranch.com/robots.txt'}

    def __init__(self):
        pass

    def check_crawl(self, producer):
        robotstxt_url = self.producers_robotstxt[producer]
        user_agent = 'MyWebScraper/1.0'
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robotstxt_url)
        rp.read()
        if rp.can_fetch(user_agent, robotstxt_url):
            return True
        else:
            return False
