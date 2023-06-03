from scraper import Producer

# Tests for Producer class
def test_producer_hopsteiner():

    user_url = 'https://www.hopsteiner.com'
    producer = Producer(user_url)

    result = producer.check_producer()

    assert result == 1


def test_producer_hollingbery():

    user_url = 'https://www.hollingberyandson.com'
    producer = Producer(user_url)

    result = producer.check_producer()

    assert result == 2


def test_producer_crosby():

    user_url = 'https://portal.crosbyhops.com'
    producer = Producer(user_url)

    result = producer.check_producer()

    assert result == 3


def test_producer_glacier():

    user_url = 'https://glacierhopsranch.com'
    producer = Producer(user_url)

    result = producer.check_producer()

    assert result == 4


def test_producer_unknown():

    user_url = 'https://www.google.com'
    producer = Producer(user_url)

    result = producer.check_producer()

    assert result == 'Nie znaleziono producenta.'
