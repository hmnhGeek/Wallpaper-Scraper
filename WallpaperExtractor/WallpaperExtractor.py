import requests, bs4
import os, random
import warnings
import progressbar

warnings.filterwarnings("ignore")

class WallpaperUp(object):
    def __init__(self, keyword):
        self.url = "https://www.wallpaperup.com"
        self.keyword = keyword

    def BuildKey(self, string):
        words = string.split(' ')
        return '+'.join(words)

    def makeURL(self):
        searchKey = self.BuildKey(self.keyword)

        searchURL = self.url + "/search/results/"+searchKey
        return searchURL

    def make_soup(self, URL):
        try:
            r = requests.get(URL)
            return bs4.BeautifulSoup(r.text)
        except:
            return None

    def find_image_html_page(self, some_url):
        coffee = self.make_soup(some_url)

        if coffee != None:
            found_images=[]
            l = coffee.findAll('a', attrs={'class':'thumb-wrp'})
            for link in l:
                found_images.append(self.url+link.attrs['href'])
            return found_images
        return None

    def findBestImages(self, num_of_pages=1):
        base_url = self.makeURL()
        results = {}

        for i in range(num_of_pages):
            results.update({i:self.find_image_html_page(base_url+'/'+str(i+1))})
        return results

    def ImagesOnPageNumber(self, page_number=1):
        if page_number == 1:
            pageURL = self.makeURL()
            images_found = self.find_image_html_page(pageURL)
        else:
            pageURL = self.makeURL()+'/'+str(page_number)
            images_found = self.find_image_html_page(pageURL)
        return images_found

    def downloadImage(self, image_url, location=None):
        cwd = os.getcwd()

        if location != None:
            if not os.path.isdir(location):
                os.mkdir(location)
            os.chdir(location)

        with open(os.path.basename(image_url), 'wb') as f:
            f.write(requests.get(image_url).content)
        return 1

    def getDownloadButton(self, html_page_of_image):
        sub_soup = self.make_soup(html_page_of_image)
        downloadButton = sub_soup.findAll('a', attrs={'class':'button bordered primary download'})
        return self.url+downloadButton[0].attrs['href']

    def downloadAllImages(self, download_location=None, page_limit=1):
        allImages = self.findBestImages(page_limit)
        buttons = []

        for i in allImages:
            print("Found {} images on page {}".format(len(allImages[i]), i+1))
            for a_url in allImages[i]:
                self.downloadImage(self.getDownloadButton(a_url), download_location)
        return 1

    def random_download(self, download_location=None, page=1):
        images_found = self.ImagesOnPageNumber(page)
        lucky_image = random.choice(images_found)
        self.downloadImage(self.getDownloadButton(lucky_image), download_location)
        return 1

    def download_single_page(self, download_location=None, page=1):
        images_available = self.ImagesOnPageNumber(page)
        print("Found {} images on the page...\n".format(len(images_available)))
        bar = progressbar.ProgressBar(maxval=100, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

        bar.start()
        for image in images_available:
            self.downloadImage(self.getDownloadButton(image), download_location)
            bar.update(((images_available.index(image)+1)/len(images_available))*100)
        bar.finish()
        return 1
