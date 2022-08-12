import re

import scrapy

sub_reddit = "shortstories"


#  scrapy crawl reddit -o reddit.jl
class RedditCrawler(scrapy.Spider):
    name = "reddit"
    allowed_domains = ["old.reddit.com"]
    start_urls = [f"https://old.reddit.com/r/{sub_reddit}/top/?sort=top&t=all"]

    def parse(self, response):
        url = response.request.url

        if not f"/r/{sub_reddit}/comments/" in url:
            for sections in response.xpath("//a[@data-event-action='title']"):
                post_link = sections.xpath(".//@href").extract()[0]
                if "/r/shortstories/comments/" in post_link:
                    yield response.follow(post_link, callback=self.parse, meta={"url": url})
                else:
                    print(" *** ERORRR *** THE LINK IS: ", post_link)

                next_page = response.xpath(".//span[@class='next-button']/a/@href").extract()[0]
                yield response.follow(next_page, callback=self.parse)
        else:
            yield {
                "upvotes": response.xpath(".//div[@class='score unvoted']/text()").extract()[0],
                "title": response.xpath(".//a[@data-event-action='title']/text()").extract()[0],
                # "flair": response.xpath(".//span[@class='linkflairlabel ']/text()").extract()[0],
                "text": response.xpath(".//div[@id='siteTable']//div[@class='md']/p/text()").extract(),
                "url": response.meta.get('url', "")
            }
