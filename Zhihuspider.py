import requests
from bs4 import BeautifulSoup


class spider():

    def get_url(url):
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }
        r = requests.get(url,headers=headers)
        return r.text

    def prase_url(res):
        soup = BeautifulSoup(res, "html.parser")
        return soup

    def write_file(sp):
        name = str(sp.title.string)
        filename = "E:\\down\\" + name + ".txt"
        try:f = open(filename, 'w+')
        except OSError:
             pass
        else:
            for child in sp.find_all("p"):
                child = str(child)
                try:f.write(child)
                except UnicodeEncodeError:
                    pass
                else:
                    f.write('\n')

            f.close()

    def start(url):
        res = spider.get_url(url)
        spider.write_file(spider.prase_url(res))



