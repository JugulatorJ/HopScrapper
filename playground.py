#
# import time
# from abc import ABC, abstractmethod
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
#
# class WebURL:
#
#     def __init__(self):
#         self.url = input("Podaj adres URL lub wpisz 'EXIT' aby zakończyć działanie programu.\nURL>>> ")
#
#     def get_url(self):
#         return self.url
#
#
# class Producer:
#
#     def __init__(self, user_url):
#         self.user_url = user_url
#
#     def check_producer(self):
#         if 'hopsteiner' in self.user_url:
#             return 1
#         elif 'hollingbery' in self.user_url:
#             return 2
#
#
# class SoupSource:
#
#     def __init__(self, user_url):
#         self.user_url = user_url
#
#     def get_source_code(self):
#         driver = webdriver.Chrome()
#         driver.get(self.user_url)
#         time.sleep(1)
#         html = driver.page_source
#         source_soup = BeautifulSoup(html, 'html.parser')
#         return source_soup
#
#
# class AbstractHopCertificate(ABC):
#
#     @abstractmethod
#     def get_lot_id(self):
#         pass
#
#     @abstractmethod
#     def get_contract_number(self):
#         pass
#
#     @abstractmethod
#     def get_hop_name(self):
#         pass
#
#     @abstractmethod
#     def get_crop_year(self):
#         pass
#
#     @abstractmethod
#     def get_alpha_acid(self):
#         pass
#
#     @abstractmethod
#     def get_beta_acid(self):
#         pass
#
#     @abstractmethod
#     def get_total_oil(self):
#         pass
#
#     @abstractmethod
#     def get_cohumulone(self):
#         pass
#
#
# class HopsteinerHopCertificate(AbstractHopCertificate):
#
#     def __init__(self, source_soup):
#         self.source_soup = source_soup
#
#
#     def get_lot_id(self):
#
#         h_steiner_lot_id = self.source_soup.select_one('#root > div > main > div > div:nth-child(2) >'
#                                                        ' div:nth-child(1) > table > tbody > tr:nth-child(1) >'
#                                                        ' td:nth-child(3)').text
#         return h_steiner_lot_id
#
#     def get_contract_number(self):
#
#         h_steiner_contract_number = self.source_soup.select_one('#root > div > main > div > div:nth-child(2) >'
#                                                                 ' div:nth-child(1) > table > tbody > tr:nth-child(3) >'
#                                                                 ' td:nth-child(3)').text
#         return h_steiner_contract_number
#
#     def get_hop_name(self):
#
#         h_steiner_hop_name = self.source_soup.select_one('#root > div > main > div > div:nth-child(2) >'
#                                                          ' div:nth-child(1) > table > tbody > tr:nth-child(7) >'
#                                                          ' td:nth-child(3)').text
#         return h_steiner_hop_name
#
#     def get_crop_year(self):
#
#         h_steiner_crop_year = self.source_soup.select_one('#root > div > main > div > div:nth-child(2) > '
#                                                           'div:nth-child(1) > table > tbody > tr:nth-child(8) > '
#                                                           'td:nth-child(3)').text
#         return h_steiner_crop_year
#
#     def get_alpha_acid(self):
#
#         h_steiner_alpha_acid = self.source_soup.find_all(class_='text-right')[1].text
#         txt_alpha_acid = str(h_steiner_alpha_acid)
#         lst_txt_alpha_acid = txt_alpha_acid.split(' ')
#         float_alpha_acid = None
#         for i in lst_txt_alpha_acid:
#             if '.' in i or ',' in i:
#                 try:
#                     float_alpha_acid = float(i)
#                 except ValueError:
#                     pass
#         if float_alpha_acid is not None:
#             return float_alpha_acid
#         else:
#             print("Nie znaleziono liczby zmiennoprzecinkowej w tekście.")
#
#     def get_beta_acid(self):
#
#         return None
#
#     def get_total_oil(self):
#
#         return None
#
#     def get_cohumulone(self):
#
#         return None
#
#
# class HolingberyHopCertificate(AbstractHopCertificate):
#
#     def __init__(self, source_soup):
#         self.source_soup = source_soup
#
#     def get_lot_id(self):
#
#         hol_ber_lot_id = self.source_soup.select_one('#certificate > div.row.justify-content-center >'
#                                                      ' div.col-lg-7.text-lg-left.text-center > div:nth-child(1) >'
#                                                      ' div.col-lg-8.col-xl-8 > h1').text
#         return hol_ber_lot_id
#
#     def get_contract_number(self):
#         pass
#         return
#
#     def get_hop_name(self):
#
#         hol_ber_hop_name = self.source_soup.select_one('#certificate > div.row.justify-content-center >'
#                                                        ' div.col-lg-7.text-lg-left.text-center > div:nth-child(2) >'
#                                                        ' div.col-lg-8.col-xl-8 > h2').text
#         return hol_ber_hop_name
#
#     def get_crop_year(self):
#
#         hol_ber_crop_year = self.source_soup.select_one('#certificate > div.row.justify-content-center >'
#                                                         ' div.col-lg-7.text-lg-left.text-center > div:nth-child(3) >'
#                                                         ' div.col-lg-8.col-xl-8 > h2').text
#         return hol_ber_crop_year
#
#     def get_alpha_acid(self):
#
#         hol_ber_alpha_acid = self.source_soup.find_all(class_='col-6')[0].text
#         txt_alpha_acid = str(hol_ber_alpha_acid)
#         lst_txt_alpha_acid = txt_alpha_acid.split(' ')
#         float_alpha_acid = None
#         for i in lst_txt_alpha_acid:
#             if '.' in i or ',' in i:
#                 try:
#                     float_alpha_acid = float(i)
#                 except ValueError:
#                     pass
#         if float_alpha_acid is not None:
#             return float_alpha_acid
#         else:
#             raise ValueError("Nie znaleziono liczby zmiennoprzecinkowej w tekście.")
#
#     def get_beta_acid(self):
#
#         hol_ber_beta_acid = self.source_soup.find_all(class_='col-6')[1].text
#         txt_beta_acid = str(hol_ber_beta_acid)
#         lst_txt_beta_acid = txt_beta_acid.split(' ')
#         float_beta_acid = None
#         for i in lst_txt_beta_acid:
#             if '.' in i or ',' in i:
#                 try:
#                     float_beta_acid = float(i)
#                 except ValueError:
#                     pass
#         if float_beta_acid is not None:
#             return float_beta_acid
#         else:
#             raise ValueError("Nie znaleziono liczby zmiennoprzecinkowej w tekście.")
#
#     def get_total_oil(self):
#
#         hol_ber_total_oil = self.source_soup.find_all(class_='col-6')[3].text
#         txt_total_oil = str(hol_ber_total_oil)
#         lst_txt_total_oil = txt_total_oil.split(' ')
#         float_total_oil = None
#         for i in lst_txt_total_oil:
#             if '.' in i or ',' in i:
#                 try:
#                     float_total_oil = float(i)
#                 except ValueError:
#                     pass
#         if float_total_oil is not None:
#             return float_total_oil
#         else:
#             raise ValueError("Nie znaleziono liczby zmiennoprzecinkowej w tekście.")
#
#     def get_cohumulone(self):
#
#         hol_ber_cohumulone = self.source_soup.find_all(class_='col-lg-5')[6].text
#         txt_cohumulone = str(hol_ber_cohumulone).replace('\n', '')
#         lst_txt_cohumolone = txt_cohumulone.split(' ')
#         float_cohumulone = None
#         for i in lst_txt_cohumolone:
#             if ',' in i or '.' in i:
#                 try:
#                     float_cohumulone = float(i)
#                 except ValueError:
#                     pass
#         if float_cohumulone is not None:
#             return float_cohumulone
#         else:
#             raise ValueError("Nie znaleziono liczby zmiennoprzecinkowej w tekście.")
#
#
# https://portal.crosbyhops.com/lotlookup?format=pellet&lotnumber=2318&fbclid=IwAR1pdRp8qz3tAHFsjBas3zR_5wddvmLKdTsXqSkBM57d7_AR5etyv-G_ZGM

