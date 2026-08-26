import pymongo,redis,requests, lxml.html
from pymongo import MongoClient
from get_novel import get_article

url = 'https://www.readnovel.com/book/21855922801825904#Catalog'
m_url = 'https://www.readnovel.com'
aim_xpath = '//*[@id="j-catalogWrap"]/div[2]/div[1]/ul/li/a'

def query(url):
    html = requests.get(url).content.decode('utf-8')

    return html


def get_url(html)->list:
    selector = lxml.html.fromstring(html)
    content = selector.xpath(aim_xpath)
    result = []
    for link in content:
        cur_a = link.xpath('./@href')
        cur_title = link.xpath('./text()')
        result.append((cur_title[0].strip(), cur_a[0]))

    return result


def save(content_li):
    client = MongoClient()
    db = client['test']
    collection = db['novel']
    redis_client = redis.Redis()
    result = []
    for item in content_li:
        cur = redis_client.sadd('novel_url',item[1])
        if cur:
            html = query(m_url + item[1])
            name, content = get_article(html)
            result.append({'name': name, 'content': content})
    collection.insert_many(result)


def main():
    source = query(url)
    text = get_url(source)
    save(text)


if __name__ == '__main__':
    main()