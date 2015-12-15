# -*- coding: utf-8 -*-
import os
import re
import requests
from StringIO import StringIO
from lxml import etree
import urllib2
from assets.handlers.data import UploadHandler
from ..models import ExpertsLoadedStorage


class PublicationsUploadHandler(UploadHandler):
    """
    Handler to load experts data from hopkinsmedicine.org
    """

    def __init__(self, engine, **kw):
        super(PublicationsUploadHandler, self).__init__(engine, **kw)
        self.host = """http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&term={term}&id={id}&rettype=xml&retmode=text"""

    def get_root(self):
        """ Get root element(relative) for parsing """
        self._root = self._data.xpath(self._selectors.get("root", False)).pop(0)
        #raise Exception(self._root)
        
    def load_data(self):
        #self._data_raw = urllib2.urlopen(self._curr_url)
        self._data = etree.parse(self._curr_url)

    def get_ids(self):
        """ Get document ids """
        self._ids = self._root.xpath("Id/text()")
        #for id in self._ids:
        self.get_documents()
            
    def get_documents(self):
        """ Get document by id """
        self._documents = []
        docs_url = self.host.format(term="".join(self.search_values), id=",".join(self._ids))
        #raise Exception(docs_url)
        docs = etree.parse(docs_url)
        docs_roots = docs.xpath("//PubmedArticleSet/PubmedArticle")
        for r in docs_roots:
            authors_xpath = r.xpath("MedlineCitation/Article/AuthorList/Author")
            authors = []
            for author in authors_xpath:
                author = {
                    "lastname": author.xpath("LastName/text()").pop(),
                    "firstname": author.xpath("ForeName/text()").pop()
                }
                authors.append(author)
            d = {
                "link": "http://www.ncbi.nlm.nih.gov/pubmed",
                "title": r.xpath("MedlineCitation/Article/ArticleTitle/text()").pop(0),
                "authors": authors,
                "pmid": r.xpath("MedlineCitation/PMID/text()").pop(0)
            }
            #raise Exception(r.xpath("MedlineCitation/Article/ArticleTitle/text()"))
            self._documents.append(d)
        
    def process_xml(self):
        """ Process received data as xml """
        self.get_ids()
        pass

    def process(self):
        """ Process data """
        for keyword in self.search_values:
            for page in range(self.paginator_start, self.paginator_end):
                self.format_url(keyword=keyword, page=page)
                # OFF FOR TESTING!!!
                self.load_data()
                if self.xml:
                    self.get_root()
                    self.process_xml()
                    #self.view_profiles()
