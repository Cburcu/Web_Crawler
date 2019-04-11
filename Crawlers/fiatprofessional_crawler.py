import os

def fiatprofessional_crawler(f, soup):
    html_tags = soup.find_all('div', {"class": "overlay"})
    for html_tag in html_tags:
        tags = html_tag.find_all('h3', {"class": "title"})
        for tag in tags:
            model = tag.text
            model_file = f.readlines()
            if model not in model_file:
                f.write(model+'\n')
                print(model)
            else:
                print('model is in models file')