import json
import os
import sys
import urllib
from bs4 import BeautifulSoup
import requests

class Google:
    def __init__(self):
        self.GOOGLE_SEARCH_URL = 'http://localhost:8050/render.html?url=https://www.google.co.jp/search'
        self.session = requests.session()
        self.session.headers.update(
        {'Usera-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; WOW64; Trident/6.0)'}
        )

    def search(self,keyword,maximum):
        print('begin searching',keyword)
        query = self.query_gen(keyword)
        return self.image_search(query,maximum)

    #検索キーワードからクエリ付与したURLを生成
    def query_gen(self,keyword):
        #search query generator
        page = 0
        while True:
            params = 
