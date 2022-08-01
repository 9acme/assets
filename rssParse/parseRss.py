import feedparser
import PyRSS2Gen
import datetime

linkList = [
    {
        'title': '掘金',
        'link': 'https://juejin.cn/',
        'description': '代码不止,掘金不停',
        'subchains': [
            'https://rss.anydoor.cf/juejin/posts/1978776660216136',
            'https://rss.anydoor.cf/juejin/posts/1943592288395479'
        ]
    },
    {
        'title': '掘金2',
        'link': 'https://juejin.cn/',
        'description': '代码不止,掘金不停',
        'subchains': [
            'https://rss.anydoor.cf/juejin/posts/1978776660216136',
            'https://rss.anydoor.cf/juejin/posts/1943592288395479'
        ]
    }
]
res = []


# 解析rss
def parseRss(link):
    rss_oschina = feedparser.parse(link)
    for entry in rss_oschina['entries']:
        temp = PyRSS2Gen.RSSItem(
            author=entry['author'],
            link=entry['link'],
            title=entry['title'],
            description=entry['summary'],
            pubDate=entry['published']
        )
        res.append(temp)


# 生成rss文件
def makeRss(item, data):
    rss = PyRSS2Gen.RSS2(
        title=item['title'],
        link=item['link'],
        description=item['description'],
        lastBuildDate=datetime.datetime.now(),
        items=data
    )
    rss.write_xml(open('rss/' + item['title'] + '.xml', "w", encoding='utf-8'), encoding='utf-8')
    pass


if __name__ == '__main__':
    for item in linkList:
        for link in item['subchains']:
            parseRss(link)
        makeRss(item, res)
        res = []
