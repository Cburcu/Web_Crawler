import os

def audi_crawler(f, soup):
    html_tags = soup.find_all('a', {"class" : "nm-navigation-header-model-link"})
    for html_tag in html_tags:
        model = html_tag.text
        model_file = f.readlines()
        if model not in model_file:
            f.write(model+'\n')
            print(model)
        else:
            print('model is in models file')