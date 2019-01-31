from bs4 import BeautifulSoup
import requests
import re
from Zhihuspider import spider


urled = []
urd = []

def get_url(url):
    urled.append(url)
    if re.match(r'https:////zhuanlan.zhihu.com/(.)*', url):
        url = "http:" + url[8:]

    else:
        pass
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r.text



def prase_url(res):
    soup = BeautifulSoup(res, "html5lib")

    prase_res(soup.prettify())

    ls = (soup.find_all("meta",itemprop="url"))
    for u in ls:
        if u["content"] not in urled:

            prase_url(get_url(u["content"]))

def prase_res(html):
    s = r'<meta content="[1-9][0-9]{3,}" itemprop="upvoteCount"/>[\s\S]*?<meta content="(.)*" itemprop="url"/>'
    s = re.compile(s)
    try:
        se = s.search(html).group()
    except AttributeError:
        pass
    else:
        ur = re.search(r'https://www.zhihu.com/question/(.)*?/answer/(\d)*', se).group()
        if ur not in urd:
            urd.append(ur)
            print(ur)
            spider.start(ur)

prase_url(get_url("https://www.zhihu.com/question/19859578/answer/44321875"))
