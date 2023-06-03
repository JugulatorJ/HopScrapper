import datetime
from greetings import Greetings
from exception_catcher import exception_catcher
from db_connector import ModifyDB
from certificates import HopsteinerHopCertificate, HolingberyHopCertificate, CrosbyHopCertificate, GlacierHopCertificate
from scraper import SoupSource, Producer, WebURL, CrawlChecker


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
            entry_id = 'h_steiner ' + str(datetime.datetime.now())
            if producer == 1:
                crawl_checker = CrawlChecker()
                while crawl_checker.check_crawl(producer):
                    print("\n" + " Producent zezwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    lot_id = HopsteinerHopCertificate(soup_source).get_lot_id()
                    contract_number = HopsteinerHopCertificate(soup_source).get_contract_number()
                    hop_name = HopsteinerHopCertificate(soup_source).get_hop_name()
                    crop_year = HopsteinerHopCertificate(soup_source).get_crop_year()
                    alpha_acid = HopsteinerHopCertificate(soup_source).get_alpha_acid()
                    beta_acid = HopsteinerHopCertificate(soup_source).get_beta_acid()
                    total_oil = HopsteinerHopCertificate(soup_source).get_total_oil()
                    cohumulone = HopsteinerHopCertificate(soup_source).get_cohumulone()
                    hopstein_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                                          'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                                          'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}
                    print(hopstein_cert_dict)
                    mysql_db_modifier.insert_data('cert_all', hopstein_cert_dict)
                    mysql_db_modifier.insert_data('allowed_cert_attempts', hopstein_cert_dict)
                    print('\n')
                    break
                else:
                    hopstein_cert_dict = {'entry_id': entry_id, 'lot_id': None, 'contract_number': None,
                                          'hop_name': None, 'crop_year': None, 'alpha_acid': None,
                                          'beta_acid': None, 'total_oil': None, 'cohumulone': None}
                    mysql_db_modifier.insert_data('cert_all', hopstein_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', hopstein_cert_dict)
                    print("\n" + " Producent nie pozwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")

            elif producer == 2:
                crawl_checker = CrawlChecker()
                entry_id = 'h_bery ' + str(datetime.datetime.now())
                while crawl_checker.check_crawl(producer):
                    print("\n" + " Producent zezwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    lot_id = HolingberyHopCertificate(soup_source).get_lot_id()
                    contract_number = HolingberyHopCertificate(soup_source).get_contract_number()
                    hop_name = HolingberyHopCertificate(soup_source).get_hop_name()
                    crop_year = HolingberyHopCertificate(soup_source).get_crop_year()
                    alpha_acid = HolingberyHopCertificate(soup_source).get_alpha_acid()
                    beta_acid = HolingberyHopCertificate(soup_source).get_beta_acid()
                    total_oil = HolingberyHopCertificate(soup_source).get_total_oil()
                    cohumulone = HolingberyHopCertificate(soup_source).get_cohumulone()
                    holingbery_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                                            'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                                            'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}
                    print(holingbery_cert_dict)
                    mysql_db_modifier.insert_data('cert_all', holingbery_cert_dict)
                    mysql_db_modifier.insert_data('allowed_cert_attempts', holingbery_cert_dict)
                    print('\n')
                    break
                else:
                    holingbery_cert_dict = {'entry_id': entry_id, 'lot_id': None, 'contract_number': None,
                                            'hop_name': None, 'crop_year': None, 'alpha_acid': None,
                                            'beta_acid': None, 'total_oil': None, 'cohumulone': None}
                    mysql_db_modifier.insert_data('cert_all', holingbery_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', holingbery_cert_dict)
                    print("\n" + " Producent nie pozwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")

            elif producer == 3:
                crawl_checker = CrawlChecker()
                entry_id = 'crosby ' + str(datetime.datetime.now())
                while crawl_checker.check_crawl(producer):
                    print("\n" + " Producent zezwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    lot_id = CrosbyHopCertificate(soup_source).get_lot_id()
                    contract_number = CrosbyHopCertificate(soup_source).get_contract_number()
                    hop_name = CrosbyHopCertificate(soup_source).get_hop_name()
                    crop_year = CrosbyHopCertificate(soup_source).get_crop_year()
                    alpha_acid = CrosbyHopCertificate(soup_source).get_alpha_acid()
                    beta_acid = CrosbyHopCertificate(soup_source).get_beta_acid()
                    total_oil = CrosbyHopCertificate(soup_source).get_total_oil()
                    cohumulone = CrosbyHopCertificate(soup_source).get_cohumulone()
                    crosby_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                                        'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                                        'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}
                    print(crosby_cert_dict)
                    mysql_db_modifier.insert_data('cert_all', crosby_cert_dict)
                    mysql_db_modifier.insert_data('allowed_cert_attempts', crosby_cert_dict)
                    print('\n')
                    break
                else:
                    crosby_cert_dict = {'entry_id': entry_id, 'lot_id': None, 'contract_number': None,
                                        'hop_name': None, 'crop_year': None, 'alpha_acid': None,
                                        'beta_acid': None, 'total_oil': None, 'cohumulone': None}
                    mysql_db_modifier.insert_data('cert_all', crosby_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', crosby_cert_dict)
                    print("\n" + " Producent nie pozwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
            elif producer == 4:
                crawl_checker = CrawlChecker()
                entry_id = 'glacier ' + str(datetime.datetime.now())
                while crawl_checker.check_crawl(producer):
                    print("\n" + " Producent zezwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
                    soup_source = SoupSource(web_url.get_url()).get_source_code()
                    lot_id = GlacierHopCertificate(soup_source).get_lot_id()
                    contract_number = GlacierHopCertificate(soup_source).get_contract_number()
                    hop_name = GlacierHopCertificate(soup_source).get_hop_name()
                    crop_year = GlacierHopCertificate(soup_source).get_crop_year()
                    alpha_acid = GlacierHopCertificate(soup_source).get_alpha_acid()
                    beta_acid = GlacierHopCertificate(soup_source).get_beta_acid()
                    total_oil = GlacierHopCertificate(soup_source).get_total_oil()
                    cohumulone = GlacierHopCertificate(soup_source).get_cohumulone()
                    glacier_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                                         'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                                         'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}
                    print(glacier_cert_dict)
                    mysql_db_modifier.insert_data('cert_all', glacier_cert_dict)
                    mysql_db_modifier.insert_data('allowed_cert_attempts', glacier_cert_dict)
                    print('\n')
                    break
                else:
                    glacier_cert_dict = {'entry_id': entry_id, 'lot_id': None, 'contract_number': None,
                                         'hop_name': None, 'crop_year': None, 'alpha_acid': None,
                                         'beta_acid': None, 'total_oil': None, 'cohumulone': None}
                    mysql_db_modifier.insert_data('cert_all', glacier_cert_dict)
                    mysql_db_modifier.insert_data('disallowed_cert_attempts', glacier_cert_dict)
                    print("\n" + " Producent nie pozwala na automatyczne pobieranie danych. ".center(76, '*')
                          + "\n")
            else:

                print("\n" + " Nie znaleziono producenta w bazie danych. Wprowadź poprawny adres URL. ".center(76, '*')
                      + "\n")


if __name__ == '__main__':
    main()
