import os

def hyundai_crawler(f, soup):
    html_tags = soup.find_all('div', {"class":"modelListWrap"})
    for html_tag in html_tags:
        tags = html_tag.find_all('p')
        for tag in tags:
            model = tag.text
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