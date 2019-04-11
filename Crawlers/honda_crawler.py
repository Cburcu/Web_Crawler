import os

def honda_crawler(f, soup):
    html_tags = soup.find_all('div', {"class":"visual-models-box"})
    for html_tag in html_tags:
        tags = html_tag.find_all('a')
        for tag in tags:
            model = tag.get('href')
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