import os

def ford_crawler(f, soup):
    html_tags = soup.find_all('a')
    for html_tag in html_tags:
        href = html_tag.get('href')
        
        if "otomobiller" in str(href):
            model = href.split('/')[3]
            model_file = f.readlines()
            if model != 'modeller':
                f.write(model+'\n')
                print(model)
            else:
                print('model is in models file')
        else:
            print('empty href\n')
            #continue