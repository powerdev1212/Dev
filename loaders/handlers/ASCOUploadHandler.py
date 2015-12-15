# -*- coding: utf-8 -*-

from assets.handlers.data import UploadHandler
from ..models import ExpertsLoadedStorage


class ASCOUploadHandler(UploadHandler):
    """
    Handler to load experts data from ASCO.com.
    """
    def __init__(self, engine, **kw):
        super(ASCOUploadHandler, self).__init__(engine, **kw)

    def insert(self):
        """ Insert data into storage """
        self._root = self.get_root()
        for i in self._root:
            storage_item = ExpertsLoadedStorage()
            for mnemo, selector in self._selectors.iteritems():
                try:
                    setattr(storage_item, mnemo, i[selector])
                except:
                    pass
            if not ExpertsLoadedStorage.objects.filter(**{k: v for k, v in storage_item.__dict__.iteritems() if k in self._selectors}).exists():
                storage_item.save()
            else:
                storage_item = ExpertsLoadedStorage.objects.get(**{k: v for k, v in storage_item.__dict__.iteritems() if k in self._selectors})
                for mnemo, selector in self._selectors.iteritems():
                    try:
                        setattr(storage_item, mnemo, i[selector])
                    except:
                        pass
                storage_item.save()
                
    def insert2(self):
        """ Insert data into storage (second edition) """
        self._root = self.get_root()
        for i in self._root:
            inner_name = " ".join([i.get("first_name", ""), i.get("LastName","")])
            if inner_name !=" ":
                try:
                    expert_loaded = ExpertsLoadedStorage.objects.get(inner_name__icontains=inner_name)
                    if experts_loaded.exists():
                        for mnemo, selector in self._selectors.iteritems():
                            try:
                                setattr(expert_loaded, mnemo, i[selector])
                            except:
                                pass
                        expert_loaded.save()
                except:
                    pass

    def process(self):
        """ Process data """
        for keyword in self.search_values:
            for page in range(self.paginator_start, self.paginator_end):
                self.format_url(keyword=keyword, page=page)
                self.load_data()
                if self.json:
                    self.process_json()
                self.insert2()
