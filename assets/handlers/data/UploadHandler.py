# -*- coding: utf-8 -*-
import urllib2
import requests
import json
from lxml import etree


class UploadHandler(object):
    """
    Handler to load experts data from json response.
    url - url of target site
    search_values = letters sequence for search
   .paginator_start =.paginator_start from .paginator_start> page
   .paginator_end =.paginator_end on .paginator_end> page
    """
    _data_raw = None
    _data = []
    _root = None
    _selectors_raw = None
    _selectors = None
    _storage = None

    def __init__(self, engine, **kw):
        self._curr_url = None
        self.data = None
        self.json = True if kw.get("datatype").lower() == "json" else False
        self.xml = True if kw.get("datatype").lower() == "xml" else False
        #self.jsondata = None
        self.url = kw.get("url")
        self.search_values = kw.get("search_values")
        self._selectors_raw = engine.selectors or None
        self.paginator_start = kw.get("paginator_start")
        self.paginator_end = kw.get("paginator_end")
        
        self.prepare_search_values()
        self.prepare_selectors()
        
    def get_root(self):
        return self._data.get(self._selectors.get("root", False), False)
        
    def prepare_search_values(self):
        """ Splitting search values. """
        self.search_values = self.search_values.split(",")
        
    def prepare_selectors(self):
        self._selectors = \
        {i.mnemo: i.value for i in self._selectors_raw.filter(active=True).order_by("rank")}

    def format_url(self, **kw):
        """ Formatting url """
        self._curr_url = self.url.format(**kw)

    def load_data(self):
        #self._data_raw = urllib2.urlopen(self._curr_url)
        self._data_raw = requests.get(self._curr_url)

    def process_json(self):
        """ Process received data as json """
        self._data = json.loads(self._data_raw.text)

    def process_xml(self):
        """ Process received data as xml """
        parser = etree.HTMLParser(remove_blank_text=True, recover=True, encoding="utf-8")
        # production
        self._data = etree.fromstring(self._data_raw.text, parser)
        # test
        #with open("/home/roman/projects/files/index.html","r") as f:
        #    self._data_raw = f
        #    self._data = etree.fromstring(self._data_raw.read(), parser)

    def process(self):
        pass
