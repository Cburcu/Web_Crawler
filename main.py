from data_files import write_html_data_to_file
from html_connection import Html_Connection
from read_file import read_brand_list

PATH ='Brand_List.txt'

brands_lines = read_brand_list(PATH)

for line in brands_lines:
    URL = line
    URL_NAME = URL.split('.')
    FOLDER_NAME = URL_NAME[1] 
    DATA_FOLDER = FOLDER_NAME+'/data.txt'

    try:
        html_connection = Html_Connection(URL, FOLDER_NAME)
        soup = html_connection.read_html()
        write_html_data_to_file(URL, soup, FOLDER_NAME)
    except:
        continue
    