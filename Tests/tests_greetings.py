import pytest
from greetings import Greetings


@pytest.fixture
def greetings():
    return Greetings()


def test_welcome(capsys, greetings):
    greetings.welcome()
    captured = capsys.readouterr()
    assert captured.out == "\nWitaj, program umożliwia automatyczne pobranie danych z certyfikatu chmielu," \
                           "\noraz zapisanie ich do bazy danych MySQL. Program posiada wbudowaną bazę obsługiwanych " \
                           "producentów.\nPrzed rozpoczęciem procesu pozyskiwania danych, program sprawdzi czy jest " \
                           "to dozwolone przez\nsprawdzenie pliku robots.txt.\n "


def test_goodbye(capsys, greetings):
    greetings.goodbye()
    captured = capsys.readouterr()
    assert captured.out == "\nDziękuję za skorzystanie z programu. Do zobaczenia!"
