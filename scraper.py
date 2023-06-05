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
            producer = 'hopsteiner'
            return producer
        elif 'hollingbery' in self.user_url:
            producer = 'hollingbery'
            return producer
        elif 'crosbyhops' in self.user_url:
            producer = 'crosbyhops'
            return producer
        elif 'glacierhops' in self.user_url:
            producer = 'glacierhops'
            return producer


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

    producers_robotstxt = {'hopsteiner': 'https://www.hopsteiner.com/robots.txt',
                           'hollingbery': 'https://www.hollingberyandson.com/robots.txt',
                           'crosbyhops': 'https://portal.crosbyhops.com/robots.txt',
                           'glacierhops': 'https://glacierhopsranch.com/robots.txt'}

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
