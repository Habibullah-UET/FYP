# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from dynamic_scraper.spiders.django_spider import DjangoSpider
from Products.models import ShoppingWebsite, Product, ProductItem


class ProductSpider(DjangoSpider):

    name = 'Product_Spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(ShoppingWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Product
        self.scraped_obj_item_class = ProductItem
        super(ProductSpider, self).__init__(self, *args, **kwargs)