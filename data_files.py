import os
from Crawlers.seat_crawler import seat_crawler
from Crawlers.audi_crawler import audi_crawler
from Crawlers.renault_crawler import renault_crawler
from Crawlers.ford_crawler import ford_crawler
from Crawlers.fiatprofessional_crawler import fiatprofessional_crawler
from Crawlers.fiat_crawler import fiat_crawler
from Crawlers.bmw_crawler import bmw_crawler
from Crawlers.honda_crawler import honda_crawler
from Crawlers.hyundai_crawler import hyundai_crawler
from Crawlers.jeep_crawler import jeep_crawler
from Crawlers.arabam_crawler import arabam_crawler

def write_html_data_to_file(URL, soup, folder_name):
    folder = 'Models/'+folder_name
    if not os.path.exists(folder):
        print('Create project' + folder)
        os.makedirs(folder)

    data_folder = folder + '/models.txt'
    f = open(data_folder, 'w+')
    f.write(URL+'\n')

    if folder_name == 'seat':
        seat_crawler(f, soup)
    elif folder_name == 'audi':
        audi_crawler(f, soup)
    elif folder_name == 'renault':
        renault_crawler(f, soup)
    elif folder_name == 'ford':
        ford_crawler(f, soup)
    elif folder_name == 'fiatprofessional':
        fiatprofessional_crawler(f, soup)
    elif folder_name == 'fiat':
        fiat_crawler(f, soup)
    elif folder_name == 'bmw':
        bmw_crawler(f, soup)
    elif folder_name == 'honda':
        honda_crawler(f, soup)
    elif folder_name == 'hyundai':
        hyundai_crawler(f, soup)
    elif folder_name == 'jeep':
        jeep_crawler(f, soup)
    elif folder_name == 'arabam':
        arabam_crawler(f, soup)

    f.close()