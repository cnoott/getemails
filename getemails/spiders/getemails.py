import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import collections
from urllib.parse import urlparse

class GetEmails(CrawlSpider):
    name = 'getemails'
    with open('http_website_list.txt', 'r') as f:
        start_urls = [url.strip() for url in f.readlines()]
#    start_urls = ['http://jerikoegel.com','none']
#    allowed_domains = ['jerikoegel.com']
    with open('nohttp_website_list.txt','r') as other_f:
        allowed_domains = [url.strip() for url in other_f.readlines()]
    '''
    def start_requests(self):
        for index, url in enumerate(self.start_urls):
            if 'none' in url:
                continue
            else:
                yield scrapy.Request(url=url, callback=parse, meta={'index':index})
    '''
    rules = (
            Rule(LinkExtractor(deny=(['houzz.com$','/blog/*']),deny_domains=(['etsy.com','medium.com','flickr.com','blog.houzz.com','houzz.com','facebook.com','google.com','godaddy.com'])), callback='parse_emails',follow=True,errback='error_h', process_request='process_request'),
    )
        
    def error_h(self, response):
        if 'none' in response.url:
            self.output.write('none')
    
    limit = 40
    scraped_count = collections.defaultdict(int)
    output = open('output_emails.csv','a+')
    email_list = []
    website_list = []
    def parse_emails(self, response):
        print('\n\n parsing email')
        tags = response.xpath('//body//text()').re(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        print('\n\n\n',tags)
        url = urlparse(response.url)[1]
        print('\n\n',url)
        for email in tags:
            if url not in self.website_list:
                self.website_list.append(url)
                if 'http' not in url:
                    self.output.write('\n{},'.format(url))
            if email not in self.email_list:
                self.email_list.append(email)
                url = response.url
                self.output.write(';{}'.format(email))
                print('\n\nwriting to file')

    def process_request(self, request):
        url = urlparse(request.url)[1]
        if self.scraped_count[url] < self.limit:
            self.scraped_count[url] += 1
            return request
        else:
            print('Limit reached for {}'.format(url))


                



