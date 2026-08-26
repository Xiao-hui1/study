import requests, lxml.html, os, csv

def query(url):
    html = requests.get(url).content.decode('utf-8')

    return html

def w_file(text):
    with open('rank.csv', 'w', encoding='GBK') as f:
        cur = csv.DictWriter(f, fieldnames=['wrap_title','name'])
        cur.writeheader()
        cur.writerows(text)


def main():
    url = 'https://www.readnovel.com/rank'
    source = query(url)
    selector = lxml.html.fromstring(source)
    xp = '/html/body/div[1]/div[2]/div[2]/div'
    ele = selector.xpath(xp)

    '''
        print(lxml.html.tostring(info[0], encoding='unicode'))
        将lxml解析后的“内存对象”重新转换回人类可读的HTML字符串，并打印出来。
        简单来说，就是把代码里的对象“翻译”成网页源码给你看。
        ** 注意使用了上述的代码之后，返回的是一个string了，后续无法再使用xpath进行提取数据， 但是info[0]还是可以 **
    '''
    content = ele[0].xpath('div')
    result = []
    for item in content:
        title = item.xpath('h3/em/text()')[0]
        name = item.xpath('div/ul/li/a/text()')
        result.append({'wrap_title': title, 'name': ','.join(name)})

    w_file(result)

main()