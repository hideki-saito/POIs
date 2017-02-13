# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class CSVkwItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')

        super(CSVkwItemExporter, self).__init__(*args, **kwargs)

# import csv
# from POIs import settings
#
# def write_to_csv(item):
#    writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
#    writer.writerow([item[key] for key in item.keys()])
#
# class WriteToCsv(object):
#     def process_item(self, item, spider):
#         write_to_csv(item)
#         return item


# class PoisPipeline(object):
#     def process_item(self, item, spider):
#         return item
