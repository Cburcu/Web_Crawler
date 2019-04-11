import os

def renault_crawler(f, soup):
    html_tags = soup.find_all('a')
    for html_tag in html_tags:
        href = html_tag.get('href')
        
        try:
            if "binek-araclar" in str(href):
                model = href.split('/')[3].split('.')[0]
                model_file = f.readlines()
                if model not in model_file:
                    f.write(model+'\n')
                    print(model)
                else:
                    print('model is in models file')
            else:
                print('empty href\n')
                #continue
        except:
            continue