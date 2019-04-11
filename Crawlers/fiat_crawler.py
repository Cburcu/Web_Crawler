import os

def fiat_crawler(f, soup):
    html_tags = soup.find_all('span', {"class":"color-red text-center margin-top-20 bold margin-bottom-5"})
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