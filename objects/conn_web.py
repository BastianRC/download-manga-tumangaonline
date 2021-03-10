from bs4 import BeautifulSoup
import urllib.request

class Connect_Web():
    def __init__(self, url_web):
        self.req = urllib.request
        self.hdr = {}

        self.soup = self.ChargeWeb(url_web)

    def ChargeWeb(self, url):
        self.hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Referer': 'https://cssspritegenerator.com',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}
		
        source_code = self.req.Request(url, headers=self.hdr)

        plain_text = self.req.urlopen(source_code, timeout=20).read()
        soup = BeautifulSoup(plain_text, features="lxml")

        return soup

if __name__ == "__main__":
    conn = Connect_Web("https://lectortmo.com/viewer/2ac0f309d89b023b4d83e95cf0a50dd5/cascade")