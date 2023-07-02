import datetime
from greetings import Greetings
from exception_catcher import exception_catcher
from db_connector import ModifyDB
from scraper import SoupSource, Producer, WebURL, CrawlChecker
from certificate_creator import CertGenerator


@exception_catcher
def main():

    Greetings.welcome()
    print("\n")
    mysql_db_modifier = ModifyDB()

    while True:

        web_url = WebURL()

        if web_url.get_url().lower() == 'exit':
            Greetings.goodbye()
            break
        else:
            producer = Producer(web_url.get_url()).check_producer()
            if producer == 'hopsteiner':
                entry_id = 'h_steiner ' + str(datetime.datetime.now())
                crawl_checker = CrawlChecker()
                cert_generator = CertGenerator(producer)
                while crawl_checker.check_crawl(producer):
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    try:
                        hop_cert_dict = cert_generator.generate_hop_cert_dict(soup_source, entry_id)
                        mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                        mysql_db_modifier.insert_data('allowed_cert_attempts', hop_cert_dict)
                        print('\n')
                    except AttributeError:
                        print('\n' + ' Nie znaleziono danych potrzebnych do utworzenia certyfikatu w programie. '
                              .center(80, '*') + '\n')
                    break
                else:
                    hop_cert_dict = cert_generator.generate_scrap_denied(entry_id)
                    mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', hop_cert_dict)
                    print('\n' + "Producent nie pozwala na automatyczne pobieranie danych. ".center(78, '*')
                          + '\n')

            elif producer == 'hollingbery':
                entry_id = 'h_bery ' + str(datetime.datetime.now())
                crawl_checker = CrawlChecker()
                cert_generator = CertGenerator(producer)
                while crawl_checker.check_crawl(producer):
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    try:
                        hop_cert_dict = cert_generator.generate_hop_cert_dict(soup_source, entry_id)
                        mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                        mysql_db_modifier.insert_data('allowed_cert_attempts', hop_cert_dict)
                        print('\n')
                    except AttributeError:
                        print('\n' + ' Nie znaleziono danych potrzebnych do utworzenia certyfikatu w programie. '
                              .center(80, '*') + '\n')
                    break
                else:
                    hop_cert_dict = cert_generator.generate_scrap_denied(entry_id)
                    mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', hop_cert_dict)
                    print("\n" + " Producent nie pozwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")

            elif producer == 'crosbyhops':
                entry_id = 'h_bery ' + str(datetime.datetime.now())
                crawl_checker = CrawlChecker()
                cert_generator = CertGenerator(producer)
                while crawl_checker.check_crawl(producer):
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    try:
                        hop_cert_dict = cert_generator.generate_hop_cert_dict(soup_source, entry_id)
                        mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                        mysql_db_modifier.insert_data('allowed_cert_attempts', hop_cert_dict)
                        print('\n')
                    except AttributeError:
                        print('\n' + ' Nie znaleziono danych potrzebnych do utworzenia certyfikatu w programie. '
                              .center(80, '*') + '\n')
                    break
                else:
                    hop_cert_dict = cert_generator.generate_scrap_denied(entry_id)
                    mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', hop_cert_dict)
                    print("\n" + " Producent nie pozwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
            elif producer == 'glacierhops':
                entry_id = 'h_bery ' + str(datetime.datetime.now())
                crawl_checker = CrawlChecker()
                cert_generator = CertGenerator(producer)
                while crawl_checker.check_crawl(producer):
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    try:
                        hop_cert_dict = cert_generator.generate_hop_cert_dict(soup_source, entry_id)
                        mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                        mysql_db_modifier.insert_data('allowed_cert_attempts', hop_cert_dict)
                        print('\n')
                    except AttributeError:
                        print('\n' + ' Nie znaleziono danych potrzebnych do utworzenia certyfikatu w programie. '
                              .center(80, '*') + '\n')
                    break
                else:
                    hop_cert_dict = cert_generator.generate_scrap_denied(entry_id)
                    mysql_db_modifier.insert_data('cert_all', hop_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', hop_cert_dict)
                    print("\n" + "Producent nie pozwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
            else:
                print("\n" + " Nie znaleziono producenta w bazie danych. Wprowadź poprawny adres URL. ".center(78, '*')
                          + "\n")


if __name__ == '__main__':
    main()
