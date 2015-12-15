# -*- coding: utf-8 -*-
import csv
import StringIO
import requests
from assets.handlers.data import UploadHandler
from loaders.models import CancerStudyLoadedStorage
from deseases.models import DeseaseItem

class CBioUploadHandler(object):
    
    _data = None
    _data_raw = None
    _studies_raw = None
    storage = CancerStudyLoadedStorage
    
    def __init__(self, **kw):
        self.url1 = kw.get("url")
        self.url2 = kw.get("url2")
        
    def load_data(self):
        self._data_raw = requests.get(self.url1).text
        
    def _process_string(self):
        self._data = []
        self._data_raw = StringIO.StringIO(self._data_raw).readlines()[1:]
        for line in self._data_raw:
            line = line.split("\t")
            line.append(self.url2.format(study_id=line[0]))
            self._data.append(line)
            
    def save_to_storage(self):
        deseases = DeseaseItem.objects.all()
        for i in self._data:
            try:
                storage_item = self.storage.objects.get(mnemo=i[0])
                for d in deseases:
                    if d.inner_name in i[1] or i[1] in d.inner_name:
                        storage_item.desease = d
                storage_item.update(mnemo=i[0], inner_name=i[1], description=i[2], link=i[3])
            except:
                storage_item = self.storage()
                storage_item.mnemo = i[0]
                storage_item.inner_name = i[1]
                storage_item.description = i[2]
                storage_item.link = i[3]
                for d in deseases:
                    if d.inner_name in i[1] or i[1] in d.inner_name:
                        storage_item.desease = d
            storage_item.save()

    def process(self):
        """ Open URL to receive studies """
        self.load_data()
        self._process_string()
        self.save_to_storage()
