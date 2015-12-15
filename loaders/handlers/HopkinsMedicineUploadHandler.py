# -*- coding: utf-8 -*-
import os
from lxml import etree
import urllib2
from assets.handlers.data import UploadHandler
from ..models import ExpertsLoadedStorage


class HopkinsMedicineUploadHandler(UploadHandler):
    """
    Handler to load experts data from hopkinsmedicine.org
    """

    def __init__(self, engine, **kw):
        super(HopkinsMedicineUploadHandler, self).__init__(engine, **kw)
        self.host = "http://www.hopkinsmedicine.org"

    def get_root(self):
        """ Get root element(relative) for parsing """
        self._root = self._data.xpath(self._selectors.get("root", False))

    def view_profiles(self):
        """ Insert data into storage """
        # self._root = self.get_root()
        for i in self._root:
            """
            Get profile link element for each root:
            1. create url + modificator
            2. open the profile
            3. process data and push to insert method
            """
            self._profile_url = \
                i.xpath(self._selectors.get("link", False))[0] \
                + "?modalPref=true"
            # opening & processing current profile
            self.process_profile()
            # profile = urllib2.urlopen(url)
            # self.insert(etree.fromstring(profile.read()))

    def process_profile(self):
        # production
        self._curr_profile_raw = urllib2.urlopen(self._profile_url)
        parser = \
            etree.HTMLParser(
                remove_blank_text=True,
                recover=True, encoding="utf-8")
        self._curr_profile = \
        etree.fromstring(self._curr_profile_raw.read(), parser)
        # test
        #with open("/home/roman/projects/files/david-abrams.html", "r") as pf:
        #    self._curr_profile = etree.fromstring(pf.read(), parser)
        self._curr_profile_root = \
            self._curr_profile.xpath(
                self._selectors.get("profile_root", False))
        self.insert()

    def insert(self):
        root = self._curr_profile_root[0]
        self.storage_item = ExpertsLoadedStorage()

        # inner_name
        inner_name = root.xpath(self._selectors.get("inner_name", False))
        self.storage_item.inner_name = \
            inner_name.pop(0).strip() if inner_name else ""

        # first_name
        self.storage_item.first_name = ""

        # last_name
        self.storage_item.last_name = ""

        # appointment
        inst = root.xpath(self._selectors.get("appointment_institute", False))
        dep = root.xpath(self._selectors.get("appointment_department", False))
        institute = \
            inst.pop(0) if inst else ""
        department = \
            dep.pop(0) if dep else ""
        self.storage_item.appointment = \
            "{0} // {1}".format(institute, department)

        # medical_educations
        me = root.xpath(self._selectors.get("medical_educations", False))
        me = " // ".join([i.strip() for i in me]) if me else ""
        self.storage_item.medical_educations = me

        # publications
        pub = root.xpath(self._selectors.get("publications", False))
        pub = " // ".join([" ".join(i.xpath("text()|em/text()"))\
                          for i in pub]) if pub else ""
        self.storage_item.publications = pub

        # profile picture
        pic = root.xpath(self._selectors.get("profile_picture", False))
        pic = self.host + pic.pop(0) if pic else ""
        self.storage_item.profile_picture = pic

        if not ExpertsLoadedStorage\
                .objects.filter(**{k: v for k, v in
                                self.storage_item.__dict__.iteritems()
                                if k in self._selectors})\
                        .exists():
                            self.storage_item.save()

    def process(self):
        """ Process data """
        for keyword in self.search_values:
            for page in range(self.paginator_start, self.paginator_end):
                self.format_url(keyword=keyword, page=page)
                # OFF FOR TESTING!!!
                self.load_data()
                if self.xml:
                    self.process_xml()
                    self.get_root()
                    self.view_profiles()
