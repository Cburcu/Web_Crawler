import os

def mercedes_benz_crawler(f, soup):
    html_tags = soup.find_all('div', {"class":"modeloverview__textPositionWrapper"})
    for html_tag in html_tags:
        tags = html_tag.find_all('p', {"class":"modeloverview__modelName"})
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
        