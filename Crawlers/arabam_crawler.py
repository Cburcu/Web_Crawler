import os

def arabam_crawler(f, soup):
    html_tags = soup.find_all('ul', {"class": "category-facet-selection-wrapper scrollable"})
    for html_tag in html_tags:
        tags = html_tag.find_all('h2', {"class": "dib"})
        for tag in tags:
            model_tags = tag.find_all('a')
            for model_tag in model_tags:
                tag_href = model_tag.get('href')
                tag_href_link = tag_href.split('/')
                model = tag_href_link[3]
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
                                            