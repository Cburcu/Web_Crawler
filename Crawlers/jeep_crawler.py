import os

def jeep_crawler(f, soup):
    html_tags = soup.find_all('h3', {"class": "footer-col-title js-footer-links"})
    for html_tag in html_tags:
        html_tag_text = html_tag.text
        if "MODELLER" in html_tag_text:
            tags = html_tag.parent.find_all('a')
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
        
        