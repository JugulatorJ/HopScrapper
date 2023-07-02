from scraper import WebURL
from scraper import Producer


def test_WebURL(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'http://example.com')

    web_url = WebURL()

    assert web_url.get_url() == 'http://example.com'


def test_Producer():
    producer = Producer('http://example.com')

    assert producer.check_producer() == None


def test_Producer_check_producer_hopsteiner():
    producer = Producer('http://hopsteiner.com')
    assert producer.check_producer() == 'hopsteiner'


def test_Producer_check_producer_hollingbery():
    producer = Producer('http://hollingbery.com')
    assert producer.check_producer() == 'hollingbery'


def test_Producer_check_producer_crosbyhops():
    producer = Producer('http://crosbyhops.com')
    assert producer.check_producer() == 'crosbyhops'


def test_Producer_check_producer_glacierhops():
    producer = Producer('http://glacierhops.com')
    assert producer.check_producer() == 'glacierhops'

