import logging
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
      if spider.conf['DO_ACTION']: #Necessary since DDS v.0.9+
            try:
                item['Website'] = spider.ref_object

                checker_rt = SchedulerRuntime(runtime_type='C')
                checker_rt.save()
                item['checker_runtime'] = checker_rt

                item.save()
                spider.action_successful = True
                spider.log("Item saved.", logging.INFO)

            except IntegrityError as e:
                spider.log(str(e), logging.ERROR)
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
      else:
          if not item.is_valid():
              spider.log(str(item._errors), logging.ERROR)
              raise DropItem("Missing attribute.")

      return item