import re, csv, requests, os, lxml
from multiprocessing.dummy import Pool
start_url = 'https://www.readnovel.com'

def get_html(html):
    url_list = []
    block = re.findall('正文卷<i>&#183;</i>(.*?)</div>', html, re.S)[0]
    total_url = re.findall('href="(.*?)"', block, re.S)
    for cur in total_url:
        url_list.append(start_url + cur)

    return url_list

def get_article(html):
    name = re.search('">(第.*?)</h1>', html, re.S).group(1)
    content =  re.findall('<div class="ywskythunderfont">(.*?)<script id="enContentLoader">', html, re.S)[0]
    text = re.findall('p>\u3000\u3000(.*?)<', content, re.S)

    return name, text

def save(name, text):
    #首先需要判断一个文件夹是否存在，不存在就要创建
    os.makedirs('Welcome', exist_ok=True)

    file_path = os.path.join('Welcome',name+'.txt')
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in text:
            f.write(item + '\n')
        f.close()

def query(url):
    aim = requests.get(url).content.decode()
    return aim

def main():
    url = 'https://www.readnovel.com/book/25001510901180504#Catalog'
    html = query(url)
    url_list = get_html(html)
    for url in url_list:
        cur = query(url)
        name, content = get_article(cur)
        save(name, content)


if __name__ == '__main__':
    main()