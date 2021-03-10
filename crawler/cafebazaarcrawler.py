import json
import requests
from abc import ABC
from crawlers.parser import Parser
from crawlers.config import payload, HEADER, BASE_URL, CATEGORIES
from threading import Thread
from queue import Queue


class BaseCrawler(ABC):
    def __init__(self, url):
        self.url = url
        self.parser = Parser()

    def post(self, category):
        payload["singleRequest"]["getPageV2Request"]["path"] = category

        try:
            response = requests.post(
                self.url,
                data=json.dumps(payload),
                headers=HEADER
            )

        except requests.HTTPError:
            return None

        if response.status_code == 200:
            return response

        return None


class CafeBazzarLinkCrawler(BaseCrawler):
    def __init__(self, url):
        super().__init__(url)

    def crawl_links(self, categories, thread_index):

        while categories.qsize():
            category = categories.get()
            response = self.post(category)

            links = self.parser.link_parser(json.loads(response.content))

            print(f'Thread: {thread_index}\t|\t'
                  f'category: {category}\t|\t'
                  f'capacity {len(links)}')

            categories.task_done()

    def run_crawler(self):
        threads_list = list()

        queue = Queue()
        [queue.put(c) for c in CATEGORIES]

        for i in range(4):
            thread = Thread(target=self.crawl_links, args=(queue, i))
            threads_list.append(thread)
            thread.start()

        for thread in threads_list:
            thread.join()

        print('All Task Done...')


crawler = CafeBazzarLinkCrawler(BASE_URL)
crawler.run_crawler()
