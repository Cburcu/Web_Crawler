import os

def bmw_crawler(f, soup):
    html_tags = soup.find_all('h4', {"class":"ds2-model-card--title ds2-no-uppercase"})
    for html_tag in html_tags:
        model = html_tag.text
        if model != None:
            model_file = f.readlines()
            if model not in model_file:
                f.write(model+'\n')
                print(model)
            else:
                print('model is in models file')
        else:
            print('empty tag\n')
            continue