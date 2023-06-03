class Greetings:

    @staticmethod
    def welcome():
        print("\nWitaj, program umożliwia automatyczne pobranie danych z certyfikatu chmielu,\n"
              "oraz zapisanie ich do bazy danych MySQL. Program posiada wbudowaną bazę obsługiwanych producentów.\n"
              "Przed rozpoczęciem procesu pozyskiwania danych, program sprawdzi czy jest to dozwolone przez\n"
              "sprawdzenie pliku robots.txt.")

    @staticmethod
    def goodbye():
        print("\nDziękuję za skorzystanie z programu. Do zobaczenia!")
