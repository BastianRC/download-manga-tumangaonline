try:
    from conn_web import Connect_Web
except:
    from objects.conn_web import Connect_Web

class Download_TMO(Connect_Web):
    def __init__(self, url):
        super().__init__(url)
        self.dirChapter = ""
        self.dataFinal = ""
        self.dirMain = ""
        self.urlWeb = url
        self.infoProject = []
        self.urlImgsCh = []

        self.DownloadImgChapter()

    def GetDataChapter(self):
        dataH1 = self.soup.find('div', class_='row align-items-center').h1.get_text()
        dataH2 = self.soup.find('div', class_='row align-items-center').h2.get_text()
        
        self.infoProject = [dataH1, dataH2]

        self.dataFinal = [dataH1.rstrip(), "{}".format(dataH2.lstrip().replace('\n', ' ').rstrip())]

        return self.dataFinal
    
    def DownloadImgChapter(self):
        infoCh = self.GetDataChapter()

        self.dirMain = infoCh[0].replace(':\xa0', ' - ')
        self.dirChapter = infoCh[1].replace(':\xa0', ' - ')

        for a in self.dirMain:
            if a == ':':
                self.dirMain = infoCh[0].replace(a, '')

        for i in self.dirChapter:
            if i == ':':
                self.dirChapter = infoCh[1].replace(i, '')

        for link in self.soup.find_all("img",{"class":"viewer-img"}):
            data = link.get("data-src")
            self.urlImgsCh.append(data)
        
        if self.urlImgsCh == []:
            source = self.req.Request(self.urlWeb, headers=self.hdr)
            r = self.req.urlopen(source, timeout=20)

            conn_try = Connect_Web(str(r.geturl()).replace('paginated', 'cascade'))

            for link in conn_try.soup.find_all("img",{"class":"viewer-img"}):
                data = link.get("data-src")
                self.urlImgsCh.append(data)

class Download_Multi_TMO(Connect_Web):
    def __init__(self, url):
        super().__init__(url)
        #print(self.GetUrlChapter())

    def GetUrlChapter(self):
        chapters = {}
        urlChs = [] 

        for index in self.soup.find_all("li",{"class":"list-group-item p-0 bg-light upload-link"}):
            for link in index.find_all("div",{"class":"col-2 col-sm-1 text-right"}):
                data = link.find('a')['href']
                urlChs.append(data)

                break
        count = 1
        for i in urlChs[::-1]:
            chapters[count] = i
            count += 1
        
        return chapters

if __name__ == "__main__":
    method = Download_Multi_TMO("https://lectortmo.com/library/manga/13096/diamond-no-ace-act-ii")