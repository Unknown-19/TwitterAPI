import requests
import re

class Twitter:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Connection': 'keep-alive',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }
        self.request = requests.Session()

    def getCookieGt(self):
        response = self.request.get('https://twitter.com/', headers=self.headers)
        res = re.search(r'document\.cookie="gt=(\d+);', response.text)
        return res

    def getCookieId(self):
        response = self.request.get('https://twitter.com/', headers=self.headers)
        res = re.search(r'document\.cookie="guest_id_marketing=([^;]+);', response.text)
        return res
        pass

    def getCookiePersonal(self):
        response = self.request.get('https://twitter.com/', headers=self.headers)
        res = re.search(r'document\.cookie="personalization_id=\\"([^;]+)\\";', response.text)
        pass
