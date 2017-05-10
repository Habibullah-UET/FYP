from __future__ import unicode_literals
import os, sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FYP.settings")
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../"))


BOT_NAME = 'Products'

LOG_STDOUT = True

SPIDER_MODULES = ['dynamic_scraper.spiders', 'Products.Scraper',]
USER_AGENT = '{b}/{v}'.format(b=BOT_NAME, v='1.0')

ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.DjangoImagesPipeline': 200,
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'Products.Scraper.pipelines.DjangoWriterPipeline': 800,
}

#IMAGES_STORE = os.path.join(PROJECT_ROOT, '../thumbnails')

# IMAGES_THUMBS = {
#     'medium': (50, 50),
#     'small': (25, 25),
# }

DSCRAPER_IMAGES_STORE_FORMAT = 'ALL'

DSCRAPER_LOG_ENABLED = True
DSCRAPER_LOG_LEVEL = 'INFO'
DSCRAPER_LOG_LIMIT = 5